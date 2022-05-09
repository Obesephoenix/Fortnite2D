import pygame as pg
from pygame.math import Vector2
from typing import Union


class Player(pg.sprite.Sprite):
    pos: Vector2
    velocity: Vector2

    def __init__(self, image: pg.Surface, pos: Union[tuple[int, int], Vector2], *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = pos if type(pos) == Vector2 else Vector2(pos)
        self.rect.center = (self.pos.x, self.pos.y)

    def update(self):
        self.pos += self.velocity
        self.rect.center = (self.pos.x, self.pos.y)
