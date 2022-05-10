import pygame as pg
from pygame.math import Vector2
from typing import Union
from entity import BasicEntity

gravity_strength = 4


class Player(BasicEntity):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]], *groups):
        super().__init__(image, pos, *groups)
        self.jumping = 0
        self.grounded = False

    def jump(self):
        if self.jumping == 0:
            self.jumping = 9.5
            self.grounded = False

    def collide(self, other: BasicEntity):
        if not self.rect.colliderect(other.rect):
            return
        poi = pg.sprite.collide_mask(self, other)
        if poi is not None:
            if poi[1] >= 96 and self.jumping < gravity_strength:
                self.grounded = True
                self.jumping = 0

    def update(self):
        self.vel.y += gravity_strength
        if self.grounded:
            self.vel.y -= gravity_strength
        if self.jumping > 0:
            self.jumping -= 0.05
        self.vel.y -= self.jumping

        super().update()

        self.vel = Vector2(0, 0)
        self.grounded = False
