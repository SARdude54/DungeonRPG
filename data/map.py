import pygame
import json

from .image import load_image
from .entities import Entity, Hero

# tile vars
FLOOR1 = load_image("assets/tiles/floors/floor_1.png", [50, 50], (255, 255, 255))
FLOOR2 = load_image("assets/tiles/floors/floor_2.png", [50, 50], (255, 255, 255))

# wall edges
WALL_CORNER = load_image("assets/tiles/walls/wall_edges/wall_corner.png", [15, 15], (255, 255, 255))
WALL_SIDE = load_image("assets/tiles/walls/wall_edges/wall_side.png", [15, 50], (255, 255, 255))
WALL_TOP_LEFT = load_image("assets/tiles/walls/wall_edges/wall_top_left.png", [50, 15], (255, 255, 255))
WALL_TOP_MID = load_image("assets/tiles/walls/wall_edges/wall_top_mid.png", [50, 15], (255, 255, 255))
WALL_TOP_RIGHT = load_image("assets/tiles/walls/wall_edges/wall_top_right.png", [50, 15], (255, 255, 255))

# wall tiles
WALL_TILE_LEFT = load_image("assets/tiles/walls/wall_tiles/wall_tile_left.png", [50, 50], (255, 255, 255))
WALL_TILE_MID = load_image("assets/tiles/walls/wall_tiles/wall_tile_mid.png", [50, 50], (255, 255, 255))
WALL_TILE_RIGHT = load_image("assets/tiles/walls/wall_tiles/wall_tile_right.png", [50, 50], (255, 255, 255))
WALL_TILE_PIECE_LEFT = load_image("assets/tiles/walls/wall_tiles/wall_tile_piece_left.png", [15, 50], (255, 255, 255))
WALL_TILE_PIECE_RIGHT = load_image("assets/tiles/walls/wall_tiles/wall_tile_piece_right.png", [15, 50], (255, 255, 255))
WALL_CORNER_EDGE_RIGHT = load_image("assets/tiles/walls/wall_edges/wall_corner_edge_right.png", [50, 50],
                                    (255, 255, 255))
WALL_CORNER_EDGE_RIGHT_FLIP = load_image("assets/tiles/walls/wall_edges/wall_corner_edge_right_flip.png", [50, 50],
                                         (255, 255, 255))
WALL_CORNER_EDGE_LEFT = load_image("assets/tiles/walls/wall_edges/wall_corner_edge_right.png", [50, 50],
                                   (255, 255, 255), flip_x=True)
WALL_CORNER_EDGE_LEFT_FLIP = load_image("assets/tiles/walls/wall_edges/wall_corner_edge_right_flip.png", [50, 50],
                                        (255, 255, 255), flip_x=True)


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
                if self.map_data[i][j]["type"] == "wall tile left" or \
                        self.map_data[i][j]["type"] == "wall tile mid" or \
                        self.map_data[i][j]["type"] == "wall tile right" or \
                        self.map_data[i][j]["type"] == "floor":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 50, 50)
                    self.tile_list.append(self.map_data[i][j])

                # wall edges
                if self.map_data[i][j]["type"] == "wall top left" or self.map_data[i][j]["type"] == "wall top mid" or \
                        self.map_data[i][j]["type"] == "wall top right":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50 + 35, 50, 15)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall bottom left" or self.map_data[i][j][
                    "type"] == "wall bottom mid" or self.map_data[i][j]["type"] == "wall bottom right":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 50, 15)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall side right" or self.map_data[i][j][
                    "type"] == "wall tile piece right":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 15, 50)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall side left" or self.map_data[i][j][
                    "type"] == "wall tile piece left":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50 + 35, i * 50, 15, 50)
                    self.tile_list.append(self.map_data[i][j])

                # wall corners
                if self.map_data[i][j]["type"] == "wall corner bottom right":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50 + 35, 15, 15)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall corner bottom left":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50 + 35, i * 50 + 35, 15, 15)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall corner top right":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 15, 15)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall corner top left":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50 + 40, i * 50, 15, 15)
                    self.tile_list.append(self.map_data[i][j])

                # wall corner edges
                if self.map_data[i][j]["type"] == "wall corner edge right":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50 - 1, i * 50, 50, 50)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall corner edge right flip":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50 + 5, 50, 50)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall corner edge left":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50 + 1, i * 50, 50, 50)
                    self.tile_list.append(self.map_data[i][j])

                if self.map_data[i][j]["type"] == "wall corner edge left flip":
                    self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 50, 50)
                    self.tile_list.append(self.map_data[i][j])

                if type(self.map_data[i][j]["type"]) is list:
                    for tile_type in self.map_data[i][j]["type"]:
                        if tile_type == "wall tile left" or \
                                tile_type == "wall tile mid" or \
                                tile_type == "wall tile right" or \
                                tile_type == "floor":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 50, 50)

                        # wall edges
                        if tile_type == "wall top left" or tile_type == "wall top mid" or tile_type == "wall top right":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50 + 35, 50, 15)

                        if tile_type == "wall bottom left" or tile_type == "wall bottom mid" or tile_type == "wall bottom right":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 50, 15)

                        if tile_type == "wall side right" or tile_type == "wall tile piece right":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 15, 50)

                        if tile_type == "wall side left" or tile_type == "wall tile piece left":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50 + 35, i * 50, 15, 50)

                        # wall corners
                        if tile_type == "wall corner bottom right":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50 + 35, 15, 15)

                        if tile_type == "wall corner top right":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 15, 15)

                        if tile_type == "wall corner top left":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50 + 35, i * 50, 15, 15)

                        if self.map_data[i][j]["type"] == "wall corner bottom left":
                            tile_type = pygame.Rect(j * 50 + 35, i * 50 + 35, 15, 15)

                        # wall corner edges
                        if tile_type == "wall corner edge right":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50 - 1, i * 50, 50, 50)

                        if tile_type == "wall corner edge right flip":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50 + 5, 50, 50)

                        if tile_type == "wall corner edge left":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50 + 1, i * 50, 50, 50)

                        if tile_type == "wall corner edge left flip":
                            self.map_data[i][j]["rect"] = pygame.Rect(j * 50, i * 50, 50, 50)

                    self.tile_list.append(self.map_data[i][j])

        self.events = {
            "idle": True,
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

            # floor types render
            if tile["type"] == "floor" and tile["num"] == 1:
                display.blit(FLOOR1, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "floor" and tile["num"] == 2:
                display.blit(FLOOR2, [tile["rect"].x, tile["rect"].y])

            # wall tile render
            if tile["type"] == "wall tile left":
                display.blit(WALL_TILE_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall tile mid":
                display.blit(WALL_TILE_MID, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall tile right":
                display.blit(WALL_TILE_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall tile piece left":
                display.blit(WALL_TILE_PIECE_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall tile piece right":
                display.blit(WALL_TILE_PIECE_RIGHT, [tile["rect"].x, tile["rect"].y])

            # wall edges render
            if tile["type"] == "wall top left":
                display.blit(WALL_TOP_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall top mid":
                display.blit(WALL_TOP_MID, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall top right":
                display.blit(WALL_TOP_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom left":
                display.blit(WALL_TOP_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom mid":
                display.blit(WALL_TOP_MID, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall bottom right":
                display.blit(WALL_TOP_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side right":
                display.blit(WALL_SIDE, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall side left":
                display.blit(WALL_SIDE, [tile["rect"].x, tile["rect"].y])

            # wall corner render
            if tile["type"] == "wall corner bottom right":
                display.blit(WALL_CORNER, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall corner bottom left":
                display.blit(WALL_CORNER, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall corner top right":
                display.blit(WALL_CORNER, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall corner top left":
                display.blit(WALL_CORNER, [tile["rect"].x, tile["rect"].y])

            # wall corner edge render
            if tile["type"] == "wall corner edge right":
                display.blit(WALL_CORNER_EDGE_RIGHT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall corner edge right flip":
                display.blit(WALL_CORNER_EDGE_RIGHT_FLIP, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall corner edge left":
                display.blit(WALL_CORNER_EDGE_LEFT, [tile["rect"].x, tile["rect"].y])

            if tile["type"] == "wall corner edge left flip":
                display.blit(WALL_CORNER_EDGE_LEFT_FLIP, [tile["rect"].x, tile["rect"].y])

            if type(tile["type"]) is list:
                if "wall tile left" in tile["type"]:
                    display.blit(WALL_TILE_LEFT, [tile["rect"].x, tile["rect"].y])

                if "wall tile mid" in tile["type"]:
                    display.blit(WALL_TILE_MID, [tile["rect"].x, tile["rect"].y])

                if "wall tile right" in tile["type"]:
                    display.blit(WALL_TILE_RIGHT, [tile["rect"].x, tile["rect"].y])

                if "wall tile piece left" in tile["type"]:
                    display.blit(WALL_TILE_PIECE_LEFT, [tile["rect"].x, tile["rect"].y])

                if "wall tile piece right" in tile["type"]:
                    display.blit(WALL_TILE_PIECE_RIGHT, [tile["rect"].x, tile["rect"].y])

                if "wall top left" in tile["type"]:
                    display.blit(WALL_TOP_LEFT, [tile["rect"].x, tile["rect"].y])

                if "wall top mid" in tile["type"]:
                    display.blit(WALL_TOP_MID, [tile["rect"].x, tile["rect"].y])

                if "wall top right" in tile["type"]:
                    display.blit(WALL_TOP_RIGHT, [tile["rect"].x, tile["rect"].y])

                if "wall bottom left" in tile["type"]:
                    display.blit(WALL_TOP_LEFT, [tile["rect"].x, tile["rect"].y])

                if "wall bottom mid" in tile["type"]:
                    display.blit(WALL_TOP_MID, [tile["rect"].x, tile["rect"].y])

                if "wall bottom right" in tile["type"]:
                    display.blit(WALL_TOP_RIGHT, [tile["rect"].x, tile["rect"].y])

                if "wall side right" in tile["type"]:
                    display.blit(WALL_SIDE, [tile["rect"].x, tile["rect"].y])

                if "wall corner bottom right" in tile["type"]:
                    display.blit(WALL_CORNER, [tile["rect"].x, tile["rect"].y])

                if "wall corner top right" in tile["type"]:
                    display.blit(WALL_CORNER, [tile["rect"].x, tile["rect"].y])

                if "wall corner top left" in tile["type"]:
                    display.blit(WALL_CORNER, [tile["rect"].x, tile["rect"].y])

                # Corner edges
                if "wall corner edge right" in tile["type"]:
                    display.blit(WALL_CORNER_EDGE_RIGHT, [tile["rect"].x, tile["rect"].y])

                if "wall corner edge right flip" in tile["type"]:
                    display.blit(WALL_CORNER_EDGE_RIGHT_FLIP, [tile["rect"].x, tile["rect"].y])

                if "wall corner edge left" in tile["type"]:
                    display.blit(WALL_CORNER_EDGE_LEFT, [tile["rect"].x, tile["rect"].y])

                if "wall corner edge left flip" in tile["type"]:
                    display.blit(WALL_CORNER_EDGE_LEFT_FLIP, [tile["rect"].x, tile["rect"].y])

    def check_tile_collisions(self, player: Hero):
        for tile in self.get_tile_list():
            if player.rect.colliderect(tile["rect"]) and ("wall" in tile["type"] or type(tile["type"]) is list) and tile not in player.current_wall_tiles_colliding:
                player.current_wall_tiles_colliding.append(tile)
                continue

        for tile in player.current_wall_tiles_colliding:
            if not player.rect.colliderect(tile["rect"]):
                player.current_wall_tiles_colliding.remove(tile)

    def translate_left(self):
        """
        moves map left
        :return: None
        """
        for tile in self.tile_list:
            tile["rect"].x += -5

    def translate_right(self):
        """
        moves map right
        :return: None
        """
        for tile in self.tile_list:
            tile["rect"].x += 5

    def translate_up(self):
        """
        moves map up
        :return: None
        """
        for tile in self.tile_list:
            tile["rect"].y += -5

    def translate_down(self):
        """
        moves map down
        :return: None
        """
        for tile in self.tile_list:
            tile["rect"].y += 5

    def get_tile_list(self):
        return self.tile_list

    def set_moving_right(self):
        self.events["idle"] = False
        self.events["right"] = True

    def set_moving_left(self):
        self.events["idle"] = False
        self.events["left"] = True

    def set_moving_down(self):
        self.events["idle"] = False
        self.events["down"] = True

    def set_moving_up(self):
        self.events["idle"] = False
        self.events["up"] = True

    def set_vertical_idle(self):
        self.events["idle"] = False
        self.events["down"] = False
        self.events["up"] = False

    def set_horizontal_idle(self):
        self.events["idle"] = False
        self.events["right"] = False
        self.events["left"] = False


def tile_collided(e: Entity, tile: pygame.Rect) -> dict[str, bool]:
    collision_list = {
        "top": False,
        "bottom": False,
        "left": False,
        "right": False
    }
    if e.rect.colliderect(tile) and e.events["up"]:
        collision_list["bottom"] = True

    if e.rect.colliderect(tile) and e.events["down"]:
        collision_list["top"] = True

    if e.rect.colliderect(tile) and e.events["left"]:
        collision_list["right"] = True

    if e.rect.colliderect(tile) and e.events["right"]:
        collision_list["left"] = True

    return collision_list
