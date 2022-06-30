import pygame as pg

import map
from player import Player
from building import BuildingType, Building, align_build_point


def draw_cursor(display: pg.Surface):
    pos = pg.mouse.get_pos()
    pg.draw.circle(display, (169, 169, 169), pos, 4)


def draw_build_preview(display: pg.Surface, player: Player, grid: list[tuple[int, int]]):
    raw_pos = map.get_closest_spawn_line(pg.mouse.get_pos(), grid)
    true_pos = align_build_point(raw_pos, player.buildmode)

    image: pg.Surface
    if player.buildmode == BuildingType.WALL:
        image = pg.surface.Surface((5, 90))
    elif player.buildmode == BuildingType.FLOOR:
        image = pg.surface.Surface((90, 5))
    else:
        image = pg.surface.Surface((90, 90), pg.SRCALPHA)

        if player.facing == 1:
            pg.draw.line(image, (0, 0, 0), (0, 90), (90, 0), 7)
        else:
            pg.draw.line(image, (0, 0, 0), (0, 0), (90, 90), 7)

    image.set_alpha(32)
    display.blit(image, true_pos)
