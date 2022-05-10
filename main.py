import pygame as pg

import player
import entity

pg.init()

screen = pg.display.set_mode((900, 600))
display = pg.Surface((900, 600))
clock = pg.time.Clock()

test_group = pg.sprite.Group()
test_player = player.Player(pg.Surface((100, 100)), (100, 100))
test_object = entity.BasicEntity(pg.Surface((800, 10)), (450, 550), test_group)
other_object = entity.BasicEntity(pg.Surface((800, 10)), (450, 300), test_group)


def poll_events():
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_k:
                print(pg.mouse.get_pos())
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                test_player.grounded = False

    if keys[pg.K_SPACE]:
        test_player.jump()

    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        test_player.vel.x += 2

    if keys[pg.K_LEFT] or keys[pg.K_a]:
        test_player.vel.x -= 2


while True:
    display.fill((255, 255, 255))

    for item in test_group.sprites():
        test_player.collide(item)

    poll_events()

    test_player.update()
    display.blit(test_player.image, test_player.rect)

    test_group.update()
    test_group.draw(display)

    screen.blit(display, (0, 0))
    pg.display.update()
    clock.tick(240)
