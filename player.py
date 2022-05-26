import pygame as pg
from pygame.math import Vector2
from typing import Union, get_origin, get_args
from entity import BasicEntity
from bullet import Bullet
from spritesheet import SpriteSheet

gravity_strength = 3


class Player(BasicEntity):

    def __init__(self, image: SpriteSheet, pos: Union[Vector2, tuple[int, int]]):
        super().__init__(image.get_frame(), pos)
        self.animation = image
        self.time = 0
        self.delay = 0
        self.jumping = 0
        self.grounded = False
        self.bullets = pg.sprite.Group()
        self.facing = 1

    def jump(self):
        if self.jumping == 0:
            self.jumping = 6
            self.grounded = False

    def move_left(self):
        self.vel.x -= 2
        if self.facing == 1:
            self.image = pg.transform.flip(self.image, True, False)
            self.facing = 0

    def move_right(self):
        self.vel.x += 2
        if self.facing == 0:
            self.image = pg.transform.flip(self.image, True, False)
            self.facing = 1

    def shoot(self, pos: Union[Vector2, tuple[int, int]], group: pg.sprite.Group):
        direction: Vector2
        if isinstance(pos, tuple):
            direction = Vector2(pos) - self.pos
        else:
            direction = pos - self.pos
        bullet = Bullet(Vector2(self.pos), direction.normalize() * 3)
        group.add(bullet)

    def collide(self, other: BasicEntity):
        if not self.rect.colliderect(other.rect):
            return
        poi = pg.sprite.collide_mask(self, other)
        if poi is not None:
            if poi[1] >= (self.rect.size[1] - 3) and self.jumping < gravity_strength:
                self.grounded = True
                self.jumping = 0

    def update(self, display: pg.Surface):
        self.delay += 1
        if self.delay == 120:
            self.image = self.animation.get_frame()
            self.mask = pg.mask.from_surface(self.image)
            if self.animation.get_frame_number() == self.animation.total_frames - 2:
                self.delay = -60
            else:
                self.delay = 0

        self.vel.y += gravity_strength
        if self.grounded:
            self.vel.y -= gravity_strength
        if self.jumping > 0:
            self.jumping -= 0.05
        self.vel.y -= self.jumping

        super().update(display)

        self.vel = Vector2(0, 0)
        self.grounded = False
