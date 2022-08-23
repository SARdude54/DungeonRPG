import pygame

from pygame.locals import *
from .image import load_image, load_animation


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.animation_count = 0
        self.FOLDER: str
        self.is_left = False
        self.image = load_image("assets/Entities/knight/male/idle/knight_m_idle_anim_f0.png", [30, 50], (0, 0, 0))
        self.rect = Rect(self.x, self.y, 50, 50)

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
    def __init__(self, x, y):
        super(Enemy, self).__init__(x, y)


class Chort(Enemy):
    def __init__(self, x, y):
        super(Chort, self).__init__(x, y)
        self.FOLDER = "assets/Entities/chort"
        self.idle = load_animation(f"{self.FOLDER}/idle", "chort_idle_anim_f0", 4, [50, 50], (0, 0, 0))
        self.run = load_animation(f"{self.FOLDER}/run", "chort_run_anim_f0", 4, [50, 50], (0, 0, 0))

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
            display.blit(self.image, [self.rect.x, self.rect.y])
            self.animation_count = 0

        if self.events["right"]:
            self.dx = 5

        self.x += self.dx


class BigDemon(Enemy):
    def __init__(self, x, y):
        super(BigDemon, self).__init__(x, y)
        self.FOLDER = "assets/Entities/BigDemon"
        self.idle = load_animation(f"{self.FOLDER}/idle", "big_demon_idle_anim_f0", 4, [75, 100], (0, 0, 0))
        self.run = load_animation(f"{self.FOLDER}/run", "big_demon_run_anim_f0", 4, [75, 100], (0, 0, 0))

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
            display.blit(self.image, [self.rect.x, self.rect.y])
            self.animation_count = 0

        if self.events["right"]:
            self.dx = 5

        self.x += self.dx


class Knight(Entity):
    def __init__(self, x, y, gender):
        super(Knight, self).__init__(x, y)
        self.FOLDER = "assets/Entities/knight"
        self.gender = gender
        # Load male assets
        self.male_idle_right = load_animation(f"{self.FOLDER}/male/idle", "knight_m_idle_anim_f0", 4, [30, 50], (0, 0, 0))
        self.male_idle_left = load_animation(f"{self.FOLDER}/male/idle", "knight_m_idle_anim_f0", 4, [30, 50], (0, 0, 0), flip_x=True)

        self.male_run_right = load_animation(f"{self.FOLDER}/male/run", "knight_m_run_anim_f0", 4, [30, 50], (0, 0, 0))
        self.male_run_left = load_animation(f"{self.FOLDER}/male/run", "knight_m_run_anim_f0", 4, [30, 50], (0, 0, 0), flip_x=True)

    def render(self, display: pygame.Surface):
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
            display.blit(self.image, [self.rect.x, self.rect.y])
            self.animation_count = 0

        if self.events["right"]:
            self.dx = 5
        elif self.events["left"]:
            self.dx = -5
        if self.events["up"]:
            self.dy = -5
        elif self.events["down"]:
            self.dy = 5
