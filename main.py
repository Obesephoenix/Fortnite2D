import pygame as pg

import entity
import player
import mouse

pg.init()

screen = pg.display.set_mode((900, 600))
display = pg.Surface((900, 600))
clock = pg.time.Clock()

pg.display.set_caption("Fortnite 2D")
pg.mouse.set_visible(False)

player_image = pg.image.load("assets/image/character.png")

world = pg.sprite.Group()
player = player.Player(pg.transform.scale(player_image, (17 * 3, 30 * 3)), (100, 100))
platform_one = entity.BasicEntity(pg.Surface((800, 5)), (450, 300))
platform_two = entity.BasicEntity(pg.Surface((800, 5)), (450, 500))
world.add(platform_one, platform_two)


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
        elif event.type == pg.MOUSEBUTTONDOWN:
            player.shoot(pg.mouse.get_pos(), world)

    if keys[pg.K_SPACE]:
        player.jump()

    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        player.vel.x += 2

    if keys[pg.K_LEFT] or keys[pg.K_a]:
        player.vel.x -= 2


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
