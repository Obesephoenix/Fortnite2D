import pygame as pg
from pygame.math import Vector2
from typing import Union, get_origin, get_args
from entity import BasicEntity
from bullet import Bullet

gravity_strength = 3


class Player(BasicEntity):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]]):
        super().__init__(image, pos)
        self.jumping = 0
        self.grounded = False
        self.bullets = pg.sprite.Group()

    def jump(self):
        if self.jumping == 0:
            self.jumping = 6
            self.grounded = False

    def shoot(self, pos: Union[Vector2, tuple[int, int]], group: pg.sprite.Group):
        direction: Vector2
        if isinstance(pos, tuple):
            direction = Vector2(pos).normalize()
        else:
            direction = pos.normalize()
        bullet = Bullet(pg.Surface((10, 10)), Vector2(self.pos), direction*3)
        group.add(bullet)

    def collide(self, other: BasicEntity):
        if not self.rect.colliderect(other.rect):
            return
        poi = pg.sprite.collide_mask(self, other)
        if poi is not None:
            if poi[1] >= (self.rect.size[1] - 4) and self.jumping < gravity_strength:
                self.grounded = True
                self.jumping = 0

    def update(self, display: pg.Surface):
        if len(self.bullets.sprites()) != 0:
            for bullet in self.bullets:
                bullet.update(display)
                display.blit(bullet.image, bullet.rect)

        self.vel.y += gravity_strength
        if self.grounded:
            self.vel.y -= gravity_strength
        if self.jumping > 0:
            self.jumping -= 0.05
        self.vel.y -= self.jumping

        super().update(display)

        self.vel = Vector2(0, 0)
        self.grounded = False
