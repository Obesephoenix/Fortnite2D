import pygame as pg
from entity import BasicEntity
from typing import Union
from pygame.math import Vector2


class Bullet(BasicEntity):

    def __init__(self, pos: Union[Vector2, tuple[int, int]], vel: Union[Vector2, tuple[int, int]]):
        super().__init__(pg.image.load("assets/image/bullet.png"), pos)
        self.vel = vel
        self.image = pg.transform.scale(self.image, (9, 3))
        self.dir = Vector2(1, 0).angle_to(self.vel)
        self.image = pg.transform.rotate(self.image, 360 - self.dir)

    def update(self, display: pg.Surface):
        super().update(display)

        if self.pos.x > display.get_width() or self.pos.y > display.get_height():
            self.kill()
