import pygame
import json

from pygame.locals import *
from .image import load_image, load_animation

# TODO: Simplify floor vars
# TODO: Organize wall assets
# TODO: Add inner walls and columns
# TODO: Decorate walls with banners and animate water fountains

# tile vars
FLOOR1 = load_image("assets/tiles/floors/floor_1.png", [50, 50], (255, 255, 255))
FLOOR2 = load_image("assets/tiles/floors/floor_2.png", [50, 50], (255, 255, 255))

WALL_LEFT = load_image("assets/tiles/wall/wall_left.png", [50, 50], (255, 255, 255))
WALL_MID = load_image("assets/tiles/wall/wall_mid.png", [50, 50], (255, 255, 255))
WALL_RIGHT = load_image("assets/tiles/wall/wall_right.png", [50, 50], (255, 255, 255))
WALL_BOTTOM = load_image("assets/tiles/wall/wall_bottom.png", [50, 50], (255, 255, 255))

WALL_SIDE_FRONT_LEFT = load_image("assets/tiles/wall/wall_side_front_left.png", [50, 50], (255, 255, 255))
WALL_SIDE_FRONT_RIGHT = load_image("assets/tiles/wall/wall_side_front_right.png", [50, 50], (255, 255, 255))

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

WALL_CORNER_BOTTOM_LEFT = load_image("assets/tiles/wall/wall_corner/wall_corner_bottom_left.png", [50, 50], (255, 255, 255))
WALL_CORNER_BOTTOM_RIGHT = load_image("assets/tiles/wall/wall_corner/wall_corner_bottom_left.png", [50, 50], (255, 255, 255), flip_y=True)
WALL_CORNER_TOP_LEFT = load_image("assets/tiles/wall/wall_corner/wall_corner_bottom_left.png", [50, 50], (255, 255, 255), flip_y=True)

WALL_CORNER_LEFT = load_image("assets/tiles/wall/wall_corner/wall_corner_left.png", [50, 50], (255, 255, 255))

CORNER_WALL_TOP_LEFT = load_image("assets/tiles/wall/wall_corner/wall_inner_corner_l_top_left.png", [50, 60], (255, 255, 255))
CORNER_WALL_TOP_RIGHT = load_image("assets/tiles/wall/wall_corner/wall_inner_corner_l_top_left.png", [50, 60], (255, 255, 255), flip_y=True)


class Map:
    def __init__(self, map_path: str):
        """
        Map object loads and renders a map from a json file
        :param map_path: str
        """
        self.map_path = map_path
        with open(self.map_path, "r") as f:
            self.map_data = json.load(f)

        self.tile_list = []

        for i in range(len(self.map_data)):
            for j in range(len(self.map_data[i])):
                if self.map_data[i][j] is not None:
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 50, 50)
                    self.map_data[i][j]["top_layer"] = None
                    self.tile_list.append(self.map_data[i][j])

        self.dx = 0
        self.dy = 0

        self.events = {
            "idle": True,
            "moving": False,
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

    def render(self, display: pygame.Surface):
        """
        renders a  map from tile list
        :param display: pygame.Surface
        :return: None
        """
        for tile in self.tile_list:
            if tile["type"] == "wall left":
                display.blit(WALL_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall mid":
                display.blit(WALL_MID, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall right":
                display.blit(WALL_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom":
                display.blit(WALL_BOTTOM, [tile["rect"].x, tile["rect"].y])

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

            if tile["type"] == "wall corner left":
                display.blit(WALL_CORNER_LEFT, [tile['rect'].x, tile['rect'].y])

            if tile["type"] == "wall corner bottom left":
                display.blit(WALL_CORNER_BOTTOM_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall corner bottom right":
                display.blit(WALL_CORNER_BOTTOM_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "floor1":
                display.blit(FLOOR1, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "floor2":
                display.blit(FLOOR2, [tile["rect"].x, tile["rect"].y])

        if self.events["right"]:
            self.dx = 5

        elif self.events["left"]:
            self.dx = -5

        if self.events["up"]:
            self.dy = -5
        elif self.events["down"]:
            self.dy = 5

        if self.events["idle"]:
            self.dx = 0
            self.dy = 0

    def translate_left(self):
        """
        moves map left
        :return: None
        """
        for tile in self.tile_list:
            tile["rect"].x += self.dx

    def translate_right(self):
        """
        moves map right
        :return: None
        """
        for tile in self.tile_list:
            tile["rect"].x += self.dx

    def translate_up(self):
        """
        moves map up
        :return: None
        """
        for tile in self.tile_list:
            tile["rect"].y += self.dy

    def translate_down(self):
        """
        moves map down
        :return: None
        """
        for tile in self.tile_list:
            tile["rect"].y += self.dy

    def get_tile_list(self):
        return self.tile_list
