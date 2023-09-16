import pygame
import sys
import time

from pygame.locals import *
from data.entities import Knight, Chort, BigDemon
from data.map import Map

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((900, 700))

level1_map = Map("data/level1_map.json")
tile_list = level1_map.get_tile_list()

# test entities
player = Knight(window.get_width() // 2, window.get_width() // 2, 30, 50, "male"
                                                                          "")
chort = Chort(100, 100, 50, 50)
big_demon = BigDemon(300, 300, 75, 100)

rendered_entities = [big_demon]

left_collision_tiles = ["wall side barrier left", "wall bottom right"]
right_collision_tiles = ["wall side barrier right", "wall bottom left"]
top_collision_tiles = ["wall mid", "wall right", "wall left", "red fountain mid", "wall goo", "blue fountain mid", "yellow banner", "red banner", "blue banner", "green banner", "door left", "door open", "door closed", "door right"]
bottom_collision_tiles = ["wall bottom", "wall bottom right", "wall bottom left"]

last_time = time.time()

if __name__ == "__main__":
    while True:
        window.fill((0, 0, 0))
        pygame.display.set_caption(str(clock.get_fps()))
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        # checks for tile collisions
        for tile in tile_list:
            if player.rect.colliderect(tile["rect"]) and (tile["type"] in left_collision_tiles):
                player.dx = 0
                if player.events["right"]:
                    player.dx = 5*dt

            if player.rect.colliderect(tile["rect"]) and (tile["type"] in right_collision_tiles):
                player.dx = 0
                if player.events["left"]:
                    player.dx = -5*dt

            if player.rect.colliderect(tile["rect"]) and (tile["type"] in top_collision_tiles):
                player.dy = 0
                if player.events["down"]:
                    player.dy = 5*dt

            if player.rect.colliderect(tile["rect"]) and (tile["type"] in bottom_collision_tiles):
                player.dy = 0
                if player.events["up"]:
                    player.dy = -5*dt

        # moves entities and map
        if player.rect.x >= window.get_width() // 2 and player.dx > 0:
            player.dx = 0
            level1_map.dx = -5
            level1_map.translate_left()
            for entity in rendered_entities:
                entity.rect.x += -5

        if player.rect.x <= window.get_width() // 2 and player.dx < 0:
            player.dx = 0
            level1_map.dx = 5
            level1_map.translate_right()
            for entity in rendered_entities:
                entity.rect.x += 5

        if player.rect.y <= window.get_height() // 2 and player.dy < 0:
            player.dy = 0
            level1_map.dy = 5
            level1_map.translate_down()
            for entity in rendered_entities:
                entity.rect.y += 5

        if player.rect.y >= window.get_height() // 2 and player.dy > 0:
            player.dy = 0
            level1_map.dy = -5
            level1_map.translate_up()
            for entity in rendered_entities:
                entity.rect.y += -5

        # updates player position
        player.rect.x += player.dx
        player.rect.y += player.dy

        player.update()

        # render entities and map
        level1_map.render(window, window.get_width(), window.get_height())
        for entity in rendered_entities:
            entity.render(window)
        player.render(window)

        # events
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_d and not player.events["left"]:
                    player.events["idle"] = False
                    player.events["right"] = True
                    player.events["moving"] = True

                    level1_map.events["idle"] = False
                    level1_map.events["left"] = True
                    level1_map.events["moving"] = True

                if event.key == K_a and not player.events["right"]:
                    player.events["idle"] = False
                    player.events["left"] = True
                    player.events["moving"] = True

                    level1_map.events["idle"] = False
                    level1_map.events["right"] = True
                    level1_map.events["moving"] = True

                if event.key == K_w and not player.events["down"]:
                    player.events["idle"] = False
                    player.events["up"] = True
                    player.events["moving"] = True

                    level1_map.events["idle"] = False
                    level1_map.events["down"] = True
                    level1_map.events["moving"] = True

                if event.key == K_s and not player.events["up"]:
                    player.events["idle"] = False
                    player.events["down"] = True
                    player.events["moving"] = True

                    level1_map.events["idle"] = False
                    level1_map.events["up"] = True
                    level1_map.events["moving"] = True

                if event.key == K_RIGHT:
                    big_demon.events["idle"] = False
                    big_demon.events["right"] = True

                if event.key == K_l:
                    player.lose_life()
                    print(player.health)

            if event.type == KEYUP:
                if event.key == K_d:
                    player.events["idle"] = True
                    player.events["right"] = False
                    player.events["moving"] = False

                    level1_map.events["idle"] = True
                    level1_map.events["left"] = False
                    level1_map.events["moving"] = False

                if event.key == K_a:
                    player.events["idle"] = True
                    player.events["left"] = False
                    player.events["moving"] = False

                    level1_map.events["idle"] = True
                    level1_map.events["right"] = False
                    level1_map.events["moving"] = False

                if event.key == K_w:
                    player.events["idle"] = True
                    player.events["up"] = False
                    player.events["moving"] = False

                    level1_map.events["idle"] = True
                    level1_map.events["down"] = False
                    level1_map.events["moving"] = False

                if event.key == K_s:
                    player.events["idle"] = True
                    player.events["down"] = False
                    player.events["moving"] = False

                    level1_map.events["idle"] = True
                    level1_map.events["up"] = False
                    level1_map.events["moving"] = False

                if event.key == K_RIGHT:
                    big_demon.events["idle"] = True
                    big_demon.events["right"] = False
                if event.key == K_l:
                    pass

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)
