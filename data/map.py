import pygame
import json

from pygame.locals import *
from .image import load_image, load_animation

FLOOR1 = load_image("assets/tiles/floors/floor_1.png", [50, 50], (255, 255, 255))
FLOOR2 = load_image("assets/tiles/floors/floor_2.png", [50, 50], (255, 255, 255))

WALL_LEFT = load_image("assets/tiles/wall/wall_left.png", [50, 50], (255, 255, 255))
WALL_MID = load_image("assets/tiles/wall/wall_mid.png", [50, 50], (255, 255, 255))
WALL_RIGHT = load_image("assets/tiles/wall/wall_right.png", [50, 50], (255, 255, 255))
WALL_BOTTOM = load_image("assets/tiles/wall/wall_mid.png", [50, 50], (255, 255, 255))

WALL_SIDE_FRONT_RIGHT = load_image("assets/tiles/wall/wall_side_front_right.png", [50, 50],
                                   (255, 255, 255))
WALL_SIDE_FRONT_LEFT = load_image("assets/tiles/wall/wall_side_front_left.png", [50, 50], (255, 255, 255))

WALL_SIDE_MID_LEFT = load_image("assets/tiles/wall/wall_side_mid_left.png", [50, 50], (255, 255, 255))
WALL_SIDE_MID_RIGHT = load_image("assets/tiles/wall/wall_side_mid_right.png", [50, 50], (255, 255, 255))

WALL_SIDE_TOP_LEFT = load_image("assets/tiles/wall/wall_side_top_left.png", [50, 50], (255, 255, 255))
WALL_SIDE_TOP_RIGHT = load_image("assets/tiles/wall/wall_side_top_right.png", [50, 50], (255, 255, 255))

WALL_SIDE_BOTTOM_LEFT = load_image("assets/tiles/wall/wall_side_top_left.png", [50, 50], (255, 255, 255),
                                   flip_y=True)
WALL_SIDE_BOTTOM_RIGHT = load_image("assets/tiles/wall/wall_side_top_right.png", [50, 50], (255, 255, 255),
                                    flip_y=True)

WALL_TOP_MID = load_image("assets/tiles/wall/wall_top_mid.png", [50, 50], (255, 255, 255))
WALL_BOTTOM_MID = load_image("assets/tiles/wall/wall_top_mid.png", [50, 50], (255, 255, 255), flip_y=True)


class Map:
    def __init__(self, map_path: str):
        self.level1_path = map_path
        with open(self.level1_path, "r") as f:
            self.level1_map = json.load(f)

        self.tile_list = []

        for i in range(len(self.level1_map)):
            for j in range(len(self.level1_map[i])):
                self.level1_map[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 50, 50)
                self.tile_list.append(self.level1_map[i][j])

    def load_level1(self, display: pygame.Surface):
        for tile in self.tile_list:
            if tile["type"] == "wall left":
                display.blit(WALL_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall mid":
                display.blit(WALL_MID, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall right":
                display.blit(WALL_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom":
                display.blit(WALL_RIGHT, [tile["rect"].x, tile["rect"].y - 38])

            if tile["type"] == "wall side front left":
                display.blit(WALL_SIDE_FRONT_LEFT, [tile["rect"].x, tile["rect"].y - 38])

            if tile["type"] == "wall side front right":
                display.blit(WALL_SIDE_FRONT_RIGHT, [tile["rect"].x, tile["rect"].y - 38])

            if tile["type"] == "wall side mid left":
                display.blit(WALL_SIDE_MID_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side mid right":
                display.blit(WALL_SIDE_MID_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side top left":
                display.blit(WALL_SIDE_TOP_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side top right":
                display.blit(WALL_SIDE_TOP_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side bottom left":
                display.blit(WALL_SIDE_BOTTOM_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side bottom right":
                display.blit(WALL_SIDE_BOTTOM_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall top mid":
                display.blit(WALL_TOP_MID, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom mid":
                display.blit(WALL_BOTTOM_MID, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "floor" and tile["num"] == 1:
                display.blit(FLOOR1, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "floor" and tile["num"] == 2:
                display.blit(FLOOR2, [tile["rect"].x, tile["rect"].y])

    def translate_left(self):
        for tile in self.tile_list:
            tile["rect"].x -= 5

    def translate_right(self):
        for tile in self.tile_list:
            tile["rect"].x += 5

    def translate_up(self):
        for tile in self.tile_list:
            tile["rect"].y -= 5

    def translate_down(self):
        for tile in self.tile_list:
            tile["rect"].y += 5

    def get_tile_list(self):
        return self.tile_list