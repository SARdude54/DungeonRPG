import pygame
import json

from .image import load_image, load_animation


# TODO: Add inner walls and columns

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

FOUNTAIN_TOP = load_image("assets/tiles/wall/wall_fountain/wall_fountain_top.png", [50, 50], (255, 255, 255))

RED_FOUNTAIN_BASIN = load_animation("assets/tiles/wall/wall_fountain/basin/red", "wall_fountain_basin_red_anim_f0", 3, [50, 50], (255, 255, 255))
RED_FOUNTAIN_MID = load_animation("assets/tiles/wall/wall_fountain/mid/red", "wall_fountain_mid_red_anim_f0", 3, [50, 50], (255, 255, 255))

red_f_mid_an_count = 0
red_f_basin_an_count = 0

BLUE_FOUNTAIN_BASIN = load_animation("assets/tiles/wall/wall_fountain/basin/blue", "wall_fountain_basin_blue_anim_f0", 3, [50, 50], (255, 255, 255))
BLUE_FOUNTAIN_MID = load_animation("assets/tiles/wall/wall_fountain/mid/blue", "wall_fountain_mid_blue_anim_f0", 3, [50, 50], (255, 255, 255))


blue_f_mid_an_count = 0
blue_f_basin_an_count = 0

WALL_GOO = load_image("assets/tiles/wall/wall_fountain/wall_goo.png", [50, 50], (255, 255, 255))
WALL_GOO_BASE = load_image("assets/tiles/wall/wall_fountain/wall_goo_base.png", [50, 50], (255, 255, 255))

BLUE_BANNER = load_image("assets/tiles/wall/wall_banner/wall_banner_blue.png", [50, 50], (255, 255, 255))
GREEN_BANNER = load_image("assets/tiles/wall/wall_banner/wall_banner_green.png", [50, 50], (255, 255, 255))
RED_BANNER = load_image("assets/tiles/wall/wall_banner/wall_banner_red.png", [50, 50], (255, 255, 255))
YELLOW_BANNER = load_image("assets/tiles/wall/wall_banner/wall_banner_yellow.png", [50, 50], (255, 255, 255))

DOOR_LEFT = load_image("assets/tiles/doors/doors_frame_left.png", [50, 75], (255, 255, 255))
DOOR_RIGHT = load_image("assets/tiles/doors/doors_frame_right.png", [50, 75], (255, 255, 255))
DOOR_TOP = load_image("assets/tiles/doors/doors_frame_top.png", [50, 50], (255, 255, 255))
DOOR_OPEN = load_image("assets/tiles/doors/doors_leaf_open.png", [50, 75], (255, 255, 255))
DOOR_CLOSED = load_image("assets/tiles/doors/doors_leaf_closed.png", [50, 75], (255, 255, 255))


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

    def render(self, display: pygame.Surface, display_width, display_height):
        """
        renders a  map from tile list
        :param display_height: int
        :param display_width: int
        :param display: pygame.Surface
        :return: None
        """

        global spike_animation_count, red_f_basin_an_count, red_f_mid_an_count, blue_f_mid_an_count, blue_f_basin_an_count

        for tile in self.tile_list:
            if -50 < tile['rect'].center[0] < display_width + 50 and -50 < tile["rect"].center[1] < display_height + 50:
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

                if tile["type"] == "blue banner":
                    display.blit(BLUE_BANNER, [tile["rect"].x, tile["rect"].y])

                if tile["type"] == "green banner":
                    display.blit(GREEN_BANNER, [tile["rect"].x, tile["rect"].y])

                if tile["type"] == "red banner":
                    display.blit(RED_BANNER, [tile["rect"].x, tile["rect"].y])

                if tile["type"] == "yellow banner":
                    display.blit(YELLOW_BANNER, [tile["rect"].x, tile["rect"].y])

                if tile["type"] == "fountain top":
                    display.blit(FOUNTAIN_TOP, [tile["rect"].x, tile['rect'].y])

                if tile["type"] == "red fountain mid":
                    if red_f_mid_an_count + 1 >= 90:
                        red_f_mid_an_count = 0
                    else:
                        display.blit(RED_FOUNTAIN_MID[red_f_mid_an_count//30], [tile['rect'].x, tile['rect'].y])
                        red_f_mid_an_count += 1

                if tile["type"] == "red fountain basin":
                    if red_f_basin_an_count + 1 >= 90:
                        red_f_basin_an_count = 0
                    else:
                        display.blit(RED_FOUNTAIN_BASIN[red_f_basin_an_count//30], [tile['rect'].x, tile['rect'].y])
                        red_f_basin_an_count += 1

                if tile["type"] == "blue fountain mid":
                    if blue_f_mid_an_count + 1 >= 90:
                        blue_f_mid_an_count = 0
                    else:
                        display.blit(BLUE_FOUNTAIN_MID[blue_f_mid_an_count//30], [tile['rect'].x, tile['rect'].y])
                        blue_f_mid_an_count += 1

                if tile["type"] == "blue fountain basin":
                    if blue_f_basin_an_count + 1 >= 90:
                        blue_f_basin_an_count = 0
                    else:
                        display.blit(BLUE_FOUNTAIN_BASIN[blue_f_basin_an_count//30], [tile['rect'].x, tile['rect'].y])
                        blue_f_basin_an_count += 1

                if tile["type"] == "wall goo":
                    display.blit(WALL_GOO, [tile["rect"].x, tile["rect"].y])

                if tile["type"] == "wall goo base":
                    display.blit(WALL_GOO_BASE, [tile["rect"].x, tile["rect"].y])

                if tile["type"] == "door right":
                    display.blit(DOOR_RIGHT, [tile["rect"].x, tile["rect"].y+25])

                if tile["type"] == "door left":
                    display.blit(DOOR_LEFT, [tile["rect"].x, tile["rect"].y+25])

                if tile["type"] == "door top":
                    display.blit(DOOR_TOP, [tile["rect"].x, tile["rect"].y+25])

                if tile["type"] == "door open":
                    display.blit(DOOR_OPEN, [tile["rect"].x, tile["rect"].y+25])

                if tile["type"] == "door closed":
                    display.blit(DOOR_CLOSED, [tile["rect"].x, tile["rect"].y+25])

                if tile["type"] == "floor1":
                    display.blit(FLOOR1, [tile["rect"].x, tile["rect"].y])

                if tile["type"] == "floor2":
                    display.blit(FLOOR2, [tile["rect"].x, tile["rect"].y])

                if tile["type"] == "spikes":
                    if spike_animation_count + 1 >= 65:
                        spike_animation_count = 0
                    else:
                        display.blit(SPIKES[spike_animation_count//16], [tile["rect"].x, tile["rect"].y])
                        spike_animation_count += 1

        if self.events["right"]:
            self.dx = 2

        elif self.events["left"]:
            self.dx = -2

        if self.events["up"]:
            self.dy = -2
        elif self.events["down"]:
            self.dy = 2

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
