import pygame as pg
from pygame.math import Vector2
from typing import Union
from entity import BasicEntity


class Player(BasicEntity):

    def __init__(self, image: pg.Surface, pos: Union[Vector2, tuple[int, int]], *groups):
        super().__init__(image, pos, *groups)

    def update(self):
        super().update()