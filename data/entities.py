import pygame

from pygame.locals import *
from .image import load_animation
from .ui import HealthBar, HotBar
from .items import *

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
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 6
        self.FOLDER: str
        self.is_left = False
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.colliding_tiles = []

        self.events = {
            "idle": True,
            "moving": False,
            "left": False,
            "right": False,
            "up": False,
            "down": False,
        }

    def render(self, display: pygame.Surface):
        pass


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
            self.dx = 0
            self.dy = 0
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

        if self.events["right"]:
            self.dx = 5

        self.x += self.dx


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
        self.rect = pygame.Rect(self.x, self.y, 75, 100)

    def render(self, display: pygame.Surface):
        """
        renders Big Demon
        :param display: pygame.Display
        :return: None
        """
        if self.animation_count + 1 >= 64:
            self.animation_count = 0

        if self.events["idle"]:
            self.dx = 0
            self.dy = 0
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

        if self.events["right"]:
            self.dx = 5

        self.x += self.dx


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

        # Load hero images
        self.male_idle_right = load_animation(f"{self.FOLDER}/male/idle", "knight_m_idle_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.male_idle_left = load_animation(f"{self.FOLDER}/male/idle", "knight_m_idle_anim_f0", 4, [self.width, self.height], (255, 255, 255), flip_x=True)

        self.male_run_right = load_animation(f"{self.FOLDER}/male/run", "knight_m_run_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.male_run_left = load_animation(f"{self.FOLDER}/male/run", "knight_m_run_anim_f0", 4, [self.width, self.height], (255, 255, 255), flip_x=True)

        self.female_idle_right = load_animation(f"{self.FOLDER}/female/idle", "knight_f_idle_anim_f0", 4,
                                              [self.width, self.height], (255, 255, 255))
        self.female_idle_left = load_animation(f"{self.FOLDER}/female/idle", "knight_f_idle_anim_f0", 4,
                                             [self.width, self.height], (255, 255, 255), flip_x=True)

        self.female_run_right = load_animation(f"{self.FOLDER}/female/run", "knight_f_run_anim_f0", 4,
                                             [self.width, self.height], (255, 255, 255))
        self.female_run_left = load_animation(f"{self.FOLDER}/female/run", "knight_f_run_anim_f0", 4,
                                            [self.width, self.height], (255, 255, 255), flip_x=True)

        self.hot_bar.add_item(BOW)
        self.hot_bar.add_item(SWORD)
        self.hot_bar.add_item(SPEAR)

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
            self.dx = 0
            self.dy = 0

            if self.gender == "male":
                if self.is_left:
                    display.blit(self.male_idle_left[self.animation_count // 16], [self.rect.x, self.rect.y])
                else:
                    display.blit(self.male_idle_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                if self.is_left:
                    display.blit(self.female_idle_left[self.animation_count // 16], [self.rect.x, self.rect.y])
                else:
                    display.blit(self.female_idle_right[self.animation_count // 16], [self.rect.x, self.rect.y])

            self.animation_count += 1

        elif self.events["right"]:
            if self.gender == "male":
                display.blit(self.male_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                display.blit(self.female_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

            self.is_left = False

        elif self.events["left"]:
            if self.gender == "male":
                display.blit(self.male_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                display.blit(self.female_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

            self.is_left = True

        elif self.events["up"]:
            if self.is_left:
                if self.gender == "male":
                    display.blit(self.male_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
                else:
                    display.blit(self.female_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                if self.gender == "male":
                    display.blit(self.male_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
                else:
                    display.blit(self.female_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

        elif self.events["down"]:
            if self.is_left:
                if self.gender == "male":
                    display.blit(self.male_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
                else:
                    display.blit(self.female_run_left[self.animation_count // 16], [self.rect.x, self.rect.y])
            else:
                if self.gender == "male":
                    display.blit(self.male_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
                else:
                    display.blit(self.female_run_right[self.animation_count // 16], [self.rect.x, self.rect.y])
            self.animation_count += 1

        else:
            if self.gender == "male":
                display.blit(self.male_idle_left[0], [self.rect.x, self.rect.y])
            else:
                display.blit(self.female_idle_left[0], [self.rect.x, self.rect.y])
            self.animation_count = 0

        if self.events["right"]:
            self.dx = 5
        elif self.events["left"]:
            self.dx = -5

        if self.events["up"]:
            self.dy = -5
        elif self.events["down"]:
            self.dy = 5

    def update(self):
        pass

