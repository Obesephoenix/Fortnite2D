import pygame as pg
from enum import Enum

from entity import AlignedObject
from pygame import Vector2
from typing import Union
from bullet import Bullet


class BuildingType(Enum):
    WALL = 0
    FLOOR = 1
    RAMP = 2


class Building(AlignedObject):

    def __init__(self, building_type: BuildingType, pos: Union[Vector2, tuple[int, int]], world: pg.sprite.Group,
                 grid: list[tuple[int, int]], direction=1):
        image: pg.Surface
        if building_type == BuildingType.WALL:
            image = pg.surface.Surface((5, 90))
        elif building_type == BuildingType.FLOOR:
            image = pg.surface.Surface((90, 5))
        else:
            image = pg.surface.Surface((90, 90), pg.SRCALPHA)
            if direction == 1:
                pg.draw.line(image, (0, 0, 0), (0, 90), (90, 0), 7)
            else:
                pg.draw.line(image, (0, 0, 0), (0, 0), (90, 90), 7)
        super().__init__(image, pos, grid)
        self.world = world
        self.building_type = building_type

    def collide(self, other):
        if isinstance(other, Bullet):
            self.world.remove(other)


def align_build_point(build_point: tuple[int, int], building_type: BuildingType):
    mouse_pos = pg.mouse.get_pos()
    pos = build_point

    if mouse_pos[1] < build_point[1] and building_type != BuildingType.FLOOR:
        pos = (build_point[0], build_point[1] - 90)

    if mouse_pos[0] < build_point[0] and building_type != BuildingType.WALL:
        pos = (build_point[0] - 90, build_point[1])

    return pos
