import pygame
import json

from pygame.locals import *
from .image import load_image, load_animation


# TODO: Create a separate map making project using pygame for ui instead tkinter
# TODO: Organize wall assets -> Test wall bottom right
# TODO: Add inner walls and columns
# TODO: Decorate walls with banners and animate water fountains

# tile vars
FLOOR1 = load_image("assets/tiles/floors/floor_1.png", [50, 50], (255, 255, 255))
FLOOR2 = load_image("assets/tiles/floors/floor_2.png", [50, 50], (255, 255, 255))

SPIKES = load_animation("assets/tiles/floors/spikes", "floor_spikes_anim_f0", 4, [50, 50], (255, 255, 255))

spike_animation_count = 0

WALL_LEFT = load_image("assets/tiles/wall/wall_left.png", [50, 50], (255, 255, 255))
WALL_MID = load_image("assets/tiles/wall/wall_mid.png", [50, 50], (255, 255, 255))
WALL_RIGHT = load_image("assets/tiles/wall/wall_right.png", [50, 50], (255, 255, 255))

WALL_BOTTOM = load_image("assets/tiles/wall/wall_bottom.png", [50, 50], (255, 255, 255))
WALL_BOTTOM_LEFT = load_image("assets/tiles/wall/wall_bottom_left.png", [50, 50], (255, 255, 255))
WALL_BOTTOM_RIGHT = load_image("assets/tiles/wall/wall_bottom_right.png", [50, 50], (255, 255, 255))


WALL_SIDE_LEFT = load_image("assets/tiles/wall/wall_side_left.png", [50, 50], (255, 255, 255))
WALL_SIDE_RIGHT = load_image("assets/tiles/wall/wall_side_left.png", [50, 50], (255, 255, 255), flip_x=True)

WALL_SIDE_BARRIER_LEFT = load_image("assets/tiles/wall/wall_side_barrier_left.png", [50, 50], (255, 255, 255))
WALL_SIDE_BARRIER_RIGHT = load_image("assets/tiles/wall/wall_side_barrier_right.png", [50, 50], (255, 255, 255))

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
        global spike_animation_count
        for tile in self.tile_list:
            if tile["type"] == "wall left":
                display.blit(WALL_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall mid":
                display.blit(WALL_MID, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall right":
                display.blit(WALL_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom":
                display.blit(WALL_BOTTOM, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom left":
                display.blit(WALL_BOTTOM_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom right":
                display.blit(WALL_BOTTOM_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side barrier left":
                display.blit(WALL_SIDE_BARRIER_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side barrier right":
                display.blit(WALL_SIDE_BARRIER_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side right":
                display.blit(WALL_SIDE_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side left":
                display.blit(WALL_SIDE_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "floor1":
                display.blit(FLOOR1, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "floor2":
                display.blit(FLOOR2, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "spikes":
                if spike_animation_count + 1 >= 64:
                    spike_animation_count = 0
                else:
                    display.blit(SPIKES[spike_animation_count//16], [tile["rect"].x, tile["rect"].y])
                    spike_animation_count += 1


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
