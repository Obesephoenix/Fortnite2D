import pygame as pg
from typing import Union
from pygame.math import Vector2

import map


class BasicEntity(pg.sprite.Sprite):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]]):
        super().__init__()
        self.test = 0
        self.image = image
        if isinstance(pos, tuple):
            self.pos = Vector2(pos)
        elif isinstance(pos, Vector2):
            self.pos = pos
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


class AlignedObject(BasicEntity):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]], grid: list[tuple[int, int]]):
        self.grid = grid
        self.origin = pos
        super().__init__(image, pos)
        self.rect.topleft = map.get_closest_spawn_line(self.origin, self.grid)

    def update(self, display: pg.Surface):
        pass
