import pygame
from util.constants import *

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.SCALED + pygame.RESIZABLE)
display = pygame.Surface(DISPLAY_SIZE)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Fortnite 2D")

brick = pygame.Surface((25, 25))
brick_rect = brick.get_rect()
brick_rect.center = (150, 100)

while True:
    display.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    brick_rect.centery += 5
    display.blit(brick, brick_rect)

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(FPS)
