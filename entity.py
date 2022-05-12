import pygame as pg
from typing import Union
from pygame.math import Vector2


class BasicEntity(pg.sprite.Sprite):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]]):
        super().__init__()
        self.test = 0
        self.image = image
        self.pos = pos if type(pos) == Vector2 else Vector2(pos)
        self.vel = Vector2(0, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
        self.mask = pg.mask.from_surface(self.image)

    def collide(self, other):
        pass

    def update(self, display: pg.Surface):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.rect.center = (self.pos.x, self.pos.y)