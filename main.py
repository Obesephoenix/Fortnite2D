import pygame
from pygame import Vector2
from util.constants import *
from util.mouse import render_crosshair
import object as obj

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.SCALED + pygame.RESIZABLE)
display = pygame.Surface(DISPLAY_SIZE)
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.display.set_caption("Fortnite 2D")

test_object = obj.Object(pygame.Surface((25, 25)), Vector2(150, 100))

while True:
    display.fill((255, 255, 255))
    render_crosshair(display, None)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    obj.update_object(test_object)
    obj.render_object(display, test_object)

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(FPS)
