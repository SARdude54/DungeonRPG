import pygame
import sys

from pygame.locals import *
from data.entities import Knight, Chort, BigDemon
from data.map import Map
from data.image import load_image

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((900, 700))

level1_map = Map("data/level1_map.json")
tile_list = level1_map.get_tile_list()

player = Knight(window.get_width() // 2, window.get_width() // 2, "male")
chort = Chort(100, 100)
big_demon = BigDemon(300, 300)

heart_frame = load_image("assets/ui/heart_frame.png", [250, 100], (255, 255, 255))
full_heart = load_image("assets/ui/heart_ui/ui_heart_full.png", [50, 50], (255, 255, 255))

rendered_entities = [chort, big_demon]


if __name__ == "__main__":
    while True:
        window.fill((0, 0, 0))
        pygame.display.set_caption(str(clock.get_fps()))

        for tile in tile_list:
            if player.rect.left == tile["rect"].right and tile["type"] == "wall side mid left":
                player.dx = 0
                if player.events["right"]:
                    player.dx = 5

            if player.rect.right - 20 >= tile["rect"].left and tile["type"] == "wall side mid right":
                player.dx = 0
                if player.events["left"]:
                    player.dx = -5

            if player.rect.bottom == tile["rect"].top and tile["type"] == "wall bottom mid":
                player.dy = 0
                if player.events["up"]:
                    player.dy = -5

            if player.rect.top + 45 == tile["rect"].bottom and tile["type"] == "wall mid":
                player.dy = 0
                if player.events["down"]:
                    player.dy = 5

        if player.rect.x >= window.get_width() // 2 and player.dx > 0:
            player.dx = 0
            level1_map.translate_left()
            for entity in rendered_entities:
                entity.rect.x -= 5

        if player.rect.x <= window.get_width() // 2 and player.dx < 0:
            player.dx = 0
            level1_map.translate_right()
            for entity in rendered_entities:
                entity.rect.x += 5

        if player.rect.y <= window.get_height() // 2 and player.dy < 0:
            player.dy = 0
            level1_map.translate_down()
            for entity in rendered_entities:
                entity.rect.y += 5

        if player.rect.y >= window.get_height() // 2 and player.dy > 0:
            player.dy = 0
            level1_map.translate_up()
            for entity in rendered_entities:
                entity.rect.y -= 5

        player.rect.x += player.dx
        player.rect.y += player.dy

        level1_map.load_level1(window)
        player.render(window)
        chort.render(window)
        big_demon.render(window)

        window.blit(heart_frame, [0, 0])
        window.blit(full_heart, [50, 30])
        window.blit(full_heart, [100, 30])
        window.blit(full_heart, [150, 30])

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_d:
                    player.events["idle"] = False
                    player.events["right"] = True

                if event.key == K_a:
                    player.events["idle"] = False
                    player.events["left"] = True

                if event.key == K_w:
                    player.events["idle"] = False
                    player.events["up"] = True

                if event.key == K_s:
                    player.events["idle"] = False
                    player.events["down"] = True

                if event.key == K_RIGHT:
                    big_demon.events["idle"] = False
                    big_demon.events["right"] = True

            if event.type == KEYUP:
                if event.key == K_d:
                    player.events["idle"] = True
                    player.events["right"] = False
                if event.key == K_a:
                    player.events["idle"] = True
                    player.events["left"] = False
                if event.key == K_w:
                    player.events["idle"] = True
                    player.events["up"] = False
                if event.key == K_s:
                    player.events["idle"] = True
                    player.events["down"] = False
                if event.key == K_RIGHT:
                    big_demon.events["idle"] = True
                    big_demon.events["right"] = False

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

