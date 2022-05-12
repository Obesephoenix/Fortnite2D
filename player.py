import pygame as pg
from pygame.math import Vector2
from typing import Union
from entity import BasicEntity
from bullet import Bullet
from copy import copy

gravity_strength = 4


class Player(BasicEntity):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]]):
        super().__init__(image, pos)
        self.jumping = 0
        self.grounded = False
        self.bullets = pg.sprite.Group()

    def jump(self):
        if self.jumping == 0:
            self.jumping = 9.5
            self.grounded = False

    def shoot(self, pos: Union[Vector2, tuple[int, int]], group: pg.sprite.Group):
        direction = pos if type(pos) == Vector2 else Vector2(pos)
        bullet = Bullet(pg.Surface((10, 10)), copy(self.pos), direction)
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
