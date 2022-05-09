import pygame as pg

pg.init()

screen = pg.display.set_mode((900, 450))
display = pg.Surface((900, 450))

while True:
    display.fill((255, 255, 255))

    screen.blit(display, (0, 0))
    pg.display.update()
