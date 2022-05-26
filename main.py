import pygame as pg

import entity
import mouse

from player import Player
from spritesheet import SpriteSheet
from entity import BasicEntity

pg.init()

screen = pg.display.set_mode((900, 600))
display = pg.Surface((900, 600))
clock = pg.time.Clock()

pg.display.set_caption("Fortnite 2D")
pg.mouse.set_visible(False)

player_image = pg.image.load("assets/image/character.png")

test_sheet_srf = pg.transform.scale(pg.image.load("assets/image/character_ambient.png"), (51 * 3, 30 * 3))
test_sheet = SpriteSheet(test_sheet_srf, (17 * 3, 30 * 3))

world = pg.sprite.Group()
player = Player(test_sheet, (100, 100))


for i in range(10):
    t = i + 1
    platform = BasicEntity(pg.Surface((800 / t, 5)), (900 - round(450 / t), 600 - t * 50))
    world.add(platform)



def poll_events():
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_k:
                print(pg.mouse.get_pos())
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                player.grounded = False
            if event.key == pg.K_r:
                player.vel = pg.math.Vector2(0, 0)
                player.pos = pg.math.Vector2(100, 100)
            if event.key == pg.K_q:
                player.shoot(pg.mouse.get_pos(), world)
        elif event.type == pg.MOUSEBUTTONDOWN:
            player.shoot(pg.mouse.get_pos(), world)

    if keys[pg.K_SPACE]:
        player.jump()

    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        player.move_right()

    if keys[pg.K_LEFT] or keys[pg.K_a]:
        player.move_left()


while True:
    display.fill((255, 255, 255))

    for item in world.sprites():
        player.collide(item)

    poll_events()

    world.update(display)
    world.draw(display)

    player.update(display)
    display.blit(player.image, player.rect)

    mouse.draw_cursor(display)
    screen.blit(display, (0, 0))
    pg.display.update()
    clock.tick(240)
