import pygame

from pygame.locals import *
from .image import load_animation
from .ui import HealthBar, HotBar

# Entity module


class Entity:
    def __init__(self, x, y, width, height):
        """
        Base class for all heroes and enemies
        :param x: int
        :param y: int
        :param width: int
        :param height: int
        """
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 6
        self.FOLDER: str
        self.is_left = False
        self.rect = Rect(x, y, self.width, self.height)
        self.current_wall_tiles_colliding = []

        self.events = {
            "idle": True,
            "left": False,
            "right": False,
            "up": False,
            "down": False,
            "collision": {
                "wall": {
                    "top": False,
                    "bottom": False,
                    "left": False,
                    "right": False
                },
                "entity": {
                    "top": False,
                    "bottom": False,
                    "left": False,
                    "right": False
                }
            }
        }

    def render(self, display: pygame.Surface):
        pass

    def check_collisions(self):
        if len(self.current_wall_tiles_colliding) != 0:
            for tile in self.current_wall_tiles_colliding:
                if tile['rect'].left < self.rect.right:
                    self.events["collision"]["wall"]["right"] = True

                if tile['rect'].right > self.rect.left:
                    self.events["collision"]["wall"]["left"] = True

        else:
            self.set_wall_collision_false()

    def set_wall_collision_false(self):
        self.events["collision"]["wall"]["top"] = False
        self.events["collision"]["wall"]["bottom"] = False
        self.events["collision"]["wall"]["left"] = False
        self.events["collision"]["wall"]["right"] = False

    def set_moving_right(self):
        self.events["idle"] = False
        self.events["right"] = True

    def set_moving_left(self):
        self.events["idle"] = False
        self.events["left"] = True

    def set_moving_up(self):
        self.events["idle"] = False
        self.events["up"] = True

    def set_moving_down(self):
        self.events["idle"] = False
        self.events["down"] = True

    def set_horizontal_idle(self):
        self.events["idle"] = True
        self.events["right"] = False
        self.events["left"] = False

    def set_vertical_idle(self):
        self.events["moving"] = True
        self.events["down"] = False
        self.events["up"] = False

    def is_wall_colliding(self):
        return self.events["collision"]["wall"]["top"] and self.events["collision"]["wall"]["bottom"] and self.events["collision"]["wall"]["right"] and self.events["collision"]["wall"]["left"]

    def is_moving_right(self):
        return not self.events["idle"] and self.events["right"]

    def is_moving_left(self):
        return not self.events["idle"] and self.events["left"]

    def is_moving_up(self):
        return not self.events["idle"] and self.events["up"]

    def is_moving_down(self):
        return not self.events["idle"] and self.events["down"]


class Enemy(Entity):
    def __init__(self, x, y, width, height):
        """
        Base class for all enemies
        :param x: int
        :param y: int
        :param width: int
        :param height: int
        """
        super(Enemy, self).__init__(x, y, width, height)


class Chort(Enemy):
    def __init__(self, x, y, width, height):
        """
        Chort enemy
        :param x: int
        :param y: int
        :param width: int
        :param height: int
        """
        super(Chort, self).__init__(x, y, width, height)
        self.FOLDER = "assets/Entities/chort"
        self.idle = load_animation(f"{self.FOLDER}/idle", "chort_idle_anim_f0", 4, [self.width, self.height], (0, 0, 0))
        self.run = load_animation(f"{self.FOLDER}/run", "chort_run_anim_f0", 4, [self.width, self.height], (0, 0, 0))

    def render(self, display: pygame.Surface):
        """
        renders chort
        :param display: pygame.Surface
        :return:
        """
        if self.animation_count + 1 >= 64:
            self.animation_count = 0

        if self.events["idle"]:
            if self.is_left:
                display.blit(self.idle[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                display.blit(self.idle[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

        elif self.events["right"]:
            display.blit(self.run[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

            self.is_left = False

        else:
            display.blit(self.idle[0], [self.rect.x, self.rect.y])
            self.animation_count = 0


class BigDemon(Enemy):
    def __init__(self, x, y, width, height):
        """
        BigDemon enemy
        :param x: int
        :param y: int
        :param width: int
        :param height: int
        """
        super(BigDemon, self).__init__(x, y, width, height)
        self.FOLDER = "assets/Entities/BigDemon"
        self.idle = load_animation(f"{self.FOLDER}/idle", "big_demon_idle_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.run = load_animation(f"{self.FOLDER}/run", "big_demon_run_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.rect = pygame.Rect(x, y, 75, 100)

    def render(self, display: pygame.Surface):
        """
        renders Big Demon
        :param display: pygame.Display
        :return: None
        """
        if self.animation_count + 1 >= 64:
            self.animation_count = 0

        if self.events["idle"]:
            if self.is_left:
                display.blit(self.idle[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                display.blit(self.idle[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

        elif self.events["right"]:
            display.blit(self.run[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

            self.is_left = False

        else:
            display.blit(self.idle[0], [self.rect.x, self.rect.y])
            self.animation_count = 0


class Hero(Entity):
    def __init__(self, x, y, width, height, gender):
        """
        Base class for heroes
        :param x: int
        :param y: int
        :param width: int
        :param height: int
        :param gender: str
        """
        super(Hero, self).__init__(x, y, width, height)
        self.gender = gender
        self.health_bar = HealthBar()
        self.hot_bar = HotBar()

    def lose_life(self):
        """
        loses one health when called
        :return: None
        """
        self.health -= 1
        self.health_bar.lose_life()


class Knight(Hero):
    def __init__(self, x, y, width, height, gender):
        """
        Knight hero
        :param x: int
        :param y: int
        :param width: int
        :param height: int
        :param gender: str
        """
        super(Knight, self).__init__(x, y, width, height, gender)
        self.FOLDER = "assets/Entities/knight"

        # Load male assets
        self.male_idle_right = load_animation(f"{self.FOLDER}/male/idle", "knight_m_idle_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.male_idle_left = load_animation(f"{self.FOLDER}/male/idle", "knight_m_idle_anim_f0", 4, [self.width, self.height], (255, 255, 255), flip_x=True)

        self.male_run_right = load_animation(f"{self.FOLDER}/male/run", "knight_m_run_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.male_run_left = load_animation(f"{self.FOLDER}/male/run", "knight_m_run_anim_f0", 4, [self.width, self.height], (255, 255, 255), flip_x=True)

    def render(self, display: pygame.Surface):
        """
        Renders knight
        :param display:
        :return:
        """
        self.health_bar.render(display)
        self.hot_bar.render(display)

        if self.animation_count + 1 >= 64:
            self.animation_count = 0

        if self.events["idle"]:
            if self.is_left:
                display.blit(self.male_idle_left[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                display.blit(self.male_idle_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

        elif self.events["right"]:
            display.blit(self.male_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

            self.is_left = False

        elif self.events["left"]:
            display.blit(self.male_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

            self.is_left = True

        elif self.events["up"]:
            if self.is_left:
                display.blit(self.male_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                display.blit(self.male_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

        elif self.events["down"]:
            if self.is_left:
                display.blit(self.male_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                display.blit(self.male_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

        else:
            display.blit(self.male_idle_left[0], [self.rect.x, self.rect.y])
            self.animation_count = 0


def collided(e1: Entity, e2: Entity) -> dict[str, bool]:
    collision_list = {
        "top": False,
        "bottom": False,
        "left": False,
        "right": False
    }
    if e1.rect.colliderect(e2.rect) and e1.events["left"]:
        collision_list["right"] = True

    if e1.rect.colliderect(e2.rect) and e1.events["right"]:
        collision_list["left"] = True

    if e1.rect.colliderect(e2.rect) and e1.events["down"]:
        collision_list["top"] = True

    if e1.rect.colliderect(e2.rect) and e1.events["up"]:
        collision_list["bottom"] = True

    return collision_list
