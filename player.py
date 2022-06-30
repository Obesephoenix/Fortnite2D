import pygame as pg
from pygame.math import Vector2
from typing import Union, get_origin, get_args

import map
from entity import BasicEntity
from bullet import Bullet
from spritesheet import SpriteSheet
from building import BuildingType, Building, align_build_point

gravity_strength = 3


class Player(BasicEntity):

    def __init__(self, image: SpriteSheet, pos: Union[Vector2, tuple[int, int]], world: pg.sprite.Group):
        super().__init__(image.get_frame(), pos)
        self.animation = image
        self.time = 0
        self.delay = 0
        self.jumping = 0
        self.bullets = pg.sprite.Group()
        self.facing = 1
        self.shooting = False
        self.world = world
        self.buildmode = None

    def jump(self):
        if self.jumping == 0:
            self.jumping = 6

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

    def shoot(self, pos: Union[Vector2, tuple[int, int]]):
        direction: Vector2
        if isinstance(pos, tuple):
            direction = Vector2(pos) - self.pos
        else:
            direction = pos - self.pos
        bullet = Bullet(Vector2(self.pos), direction.normalize() * 3)
        self.world.add(bullet)

    def build(self, building_type: BuildingType, grid: list[tuple[int, int]]):
        mouse_pos = pg.mouse.get_pos()
        build_point = map.get_closest_spawn_line(mouse_pos, grid)

        final_point = align_build_point(build_point, building_type)

        building = Building(building_type, final_point, self.world, grid, self.facing)
        self.world.add(building)

    def collide(self, other: BasicEntity):
        if not self.rect.colliderect(other.rect):
            return
        poi = pg.sprite.collide_mask(self, other)
        if poi is not None:
            if poi[1] >= (self.rect.size[1] - 3) and self.jumping < gravity_strength:
                self.jumping = 0
                self.vel.y -= gravity_strength

            elif isinstance(other, Building):
                if other.building_type == BuildingType.RAMP:
                    self.vel.y -= 4
                    if self.facing == 0:
                        self.vel.x += 3
                    else:
                        self.vel.x -= 3

    def update(self, display: pg.Surface):

        self.vel.y += gravity_strength
        if self.jumping > 0:
            self.jumping -= 0.05
        self.vel.y -= self.jumping

        super().update(display)

        self.vel = Vector2(0, 0)
