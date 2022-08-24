import pygame

from pygame.locals import *
from .image import load_animation
from .ui import HealthBar, HotBar


class Entity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height
        self.animation_count = 0
        self.FOLDER: str
        self.is_left = False
        self.rect = Rect(self.x, self.y, self.width, self.height)

        self.events = {
            "idle": True,
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

    def render(self, display: pygame.Surface):
        pass


class Enemy(Entity):
    def __init__(self, x, y, width, height):
        super(Enemy, self).__init__(x, y, width, height)


class Chort(Enemy):
    def __init__(self, x, y, width, height):
        super(Chort, self).__init__(x, y, width, height)
        self.FOLDER = "assets/Entities/chort"
        self.idle = load_animation(f"{self.FOLDER}/idle", "chort_idle_anim_f0", 4, [self.width, self.height], (0, 0, 0))
        self.run = load_animation(f"{self.FOLDER}/run", "chort_run_anim_f0", 4, [self.width, self.height], (0, 0, 0))

    def render(self, display: pygame.Surface):
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
            display.blit(self.idle, [self.rect.x, self.rect.y])
            self.animation_count = 0

        if self.events["right"]:
            self.dx = 5

        self.x += self.dx


class BigDemon(Enemy):
    def __init__(self, x, y, width, height):
        super(BigDemon, self).__init__(x, y, width, height)
        self.FOLDER = "assets/Entities/BigDemon"
        self.idle = load_animation(f"{self.FOLDER}/idle", "big_demon_idle_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.run = load_animation(f"{self.FOLDER}/run", "big_demon_run_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.rect = pygame.Rect(self.x, self.y, 75, 100)

    def render(self, display: pygame.Surface):
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
            display.blit(self.idle, [self.rect.x, self.rect.y])
            self.animation_count = 0

        if self.events["right"]:
            self.dx = 5

        self.x += self.dx


class Knight(Entity):
    def __init__(self, x, y, width, height, gender):
        super(Knight, self).__init__(x, y, width, height)
        self.FOLDER = "assets/Entities/knight"
        self.gender = gender
        self.health = 6
        self.health_bar = HealthBar()
        self.hot_bar = HotBar()
        # Load male assets
        self.male_idle_right = load_animation(f"{self.FOLDER}/male/idle", "knight_m_idle_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.male_idle_left = load_animation(f"{self.FOLDER}/male/idle", "knight_m_idle_anim_f0", 4, [self.width, self.height], (255, 255, 255), flip_x=True)

        self.male_run_right = load_animation(f"{self.FOLDER}/male/run", "knight_m_run_anim_f0", 4, [self.width, self.height], (255, 255, 255))
        self.male_run_left = load_animation(f"{self.FOLDER}/male/run", "knight_m_run_anim_f0", 4, [self.width, self.height], (255, 255, 255), flip_x=True)

        self.rect = pygame.Rect(self.x, self.y, 30, 50)

    def render(self, display: pygame.Surface):
        self.health_bar.render(display)
        self.hot_bar.render(display)
        if self.animation_count + 1 >= 64:
            self.animation_count = 0

        if self.events["idle"]:
            self.dx = 0
            self.dy = 0
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
            display.blit(self.male_idle_left, [self.rect.x, self.rect.y])
            self.animation_count = 0

        if self.events["right"]:
            self.dx = 5
        elif self.events["left"]:
            self.dx = -5
        if self.events["up"]:
            self.dy = -5
        elif self.events["down"]:
            self.dy = 5

    def lose_life(self):
        self.health -= 1
        self.health_bar.lose_life()
