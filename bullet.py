import pygame as pg
from entity import BasicEntity
from typing import Union
from pygame.math import Vector2


class Bullet(BasicEntity):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]], vel: Union[Vector2, tuple[int, int]]):
        super().__init__(image, pos)
        self.vel = vel
        print(vel)

    def update(self, display: pg.Surface):
        super().update(display)
