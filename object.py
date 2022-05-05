import pygame
from pygame import Vector2
from dataclasses import dataclass, field
from util.constants import GRAVITY_STRENGTH


@dataclass
class Object:
    image: pygame.Surface
    pos: Vector2
    vel: Vector2 = field(default=Vector2(0, 0))
    rect: pygame.Rect = field(init=False, repr=False)

    def __post_init__(self):
        self.rect = self.image.get_rect()


def apply_gravity(obj: Object):
    obj.vel = Vector2((0, 1))


def calculate_movement(obj: Object):
    obj.pos += obj.vel
    obj.vel = Vector2(0, 0)


def render_object(display: pygame.Surface, obj: Object):
    obj.rect.center = obj.pos
    display.blit(obj.image, obj.rect)
