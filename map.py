import pygame as pg

from math import floor


def draw_spawn_space(display: pg.Surface):
    for x in range(floor(display.get_width() / 90)):
        for y in range(floor(display.get_height() / 90)):
            pg.draw.rect(display, (255, 0, 0), pg.Rect((90 * x, 90 * y), (90, 90)), 2)


def gen_spawn_space(display: pg.Surface):
    res = []
    for x in range(floor(display.get_width() / 90)):
        for y in range(floor(display.get_height() / 90)):
            res.append((x * 90, y * 90))
    res.append((res[-1][0] + 90, res[-1][1] + 90))
    return res


def get_closest_spawn_line(pos: tuple[int, int], grid: list[tuple[int, int]]):
    x_point = min([x[0] for x in grid], key=lambda i: abs(pos[0] - i))
    y_point = min([y[1] for y in grid], key=lambda i: abs(pos[1] - i))

    return tuple([x_point, y_point])
