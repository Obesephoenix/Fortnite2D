import pygame
from typing import Optional


def render_crosshair(display: pygame.Surface, crosshair: Optional[pygame.Surface]):
    mouse_pos = pygame.mouse.get_pos()

    if crosshair is None:
        pygame.draw.circle(display, (211, 211, 211), mouse_pos, 6)
    else:
        display.blit(crosshair, mouse_pos)
