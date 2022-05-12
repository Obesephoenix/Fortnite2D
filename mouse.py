import pygame as pg


def draw_cursor(display: pg.Surface):
    pos = pg.mouse.get_pos()
    pg.draw.circle(display, (169, 169, 169), pos, 4)
