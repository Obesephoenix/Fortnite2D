import pygame
from pygame import Vector2
from dataclasses import dataclass, field
from util.constants import GRAVITY_STRENGTH
from typing import Union


@dataclass
class Object:
    image: pygame.Surface
    pos: Vector2
    vel: Vector2 = field(default=Vector2(0, GRAVITY_STRENGTH))
    rect: pygame.Rect = field(init=False, repr=False)

    def __post_init__(self):
        self.rect = self.image.get_rect()


def update_object(obj: Union[Object, list[Object]]):
    if type(obj) == Object:
        obj.pos += obj.vel
        obj.rect.center = obj.pos
    else:
        for item in obj:
            update_object(item)


def render_object(display: pygame.Surface, obj: Object):
    display.blit(obj.image, obj.rect)
