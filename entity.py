import pygame as pg
from typing import Union
from pygame.math import Vector2

class BasicEntity(pg.sprite.Sprite):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]], *groups):
        self.image = image
        self.pos = pos if type(pos) == Vector2 else Vector2(pos)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)