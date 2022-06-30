import pygame as pg

import mouse
import map

from player import Player
from spritesheet import SpriteSheet
from entity import AlignedObject
from building import BuildingType, Building

pg.init()

screen = pg.display.set_mode((900, 630))
display = pg.Surface((900, 630))
clock = pg.time.Clock()

pg.display.set_caption("Fortnite 2D")
pg.mouse.set_visible(False)

player_image = pg.image.load("assets/image/character.png")

test_sheet_srf = pg.transform.scale(pg.image.load("assets/image/character_ambient.png"), (51 * 3, 30 * 3))
test_sheet = SpriteSheet(test_sheet_srf, (17 * 3, 30 * 3))

world = pg.sprite.Group()
player = Player(test_sheet, (100, 100), world)
grid = map.gen_spawn_space(display)

platform = AlignedObject(pg.Surface((750, 5)), (50, 560), grid)
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

            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                player.grounded = False

            elif event.key == pg.K_r:
                player.vel = pg.math.Vector2(0, 0)
                player.pos = pg.math.Vector2(100, 100)
                for thing in world:
                    if isinstance(thing, Building):
                        world.remove(thing)

            elif event.key == pg.K_q:
                player.shoot(pg.mouse.get_pos())

            elif event.key == pg.K_1:
                player.buildmode = BuildingType.WALL if player.buildmode is not BuildingType.WALL else None
            elif event.key == pg.K_2:
                player.buildmode = BuildingType.FLOOR if player.buildmode is not BuildingType.FLOOR else None
            elif event.key == pg.K_3:
                player.buildmode = BuildingType.RAMP if player.buildmode is not BuildingType.RAMP else None

        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_buttons = pg.mouse.get_pressed(3)

            if mouse_buttons[0]:
                if player.buildmode is None:
                    player.shoot(pg.mouse.get_pos())
                else:
                    player.build(player.buildmode, grid)

    if keys[pg.K_SPACE]:
        player.jump()

    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        player.move_right()

    if keys[pg.K_LEFT] or keys[pg.K_a]:
        player.move_left()


while True:
    display.fill((255, 255, 255))
    # map.draw_spawn_space(display)

    for item in world.sprites():
        player.collide(item)

        if isinstance(item, Building):
            for obj in world:
                if obj.rect.colliderect(item.rect):
                    item.collide(obj)

    poll_events()

    world.update(display)
    world.draw(display)

    player.update(display)
    display.blit(player.image, player.rect)

    if player.buildmode is None:
        mouse.draw_cursor(display)
    else:
        mouse.draw_build_preview(display, player, grid)

    screen.blit(display, (0, 0))
    pg.display.update()
    clock.tick(240)
