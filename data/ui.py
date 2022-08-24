import pygame

from pygame.locals import *
from .image import load_image


class HealthBar:
    def __init__(self):
        self.heart_frame = load_image("assets/ui/frame/heart_frame.png", [250, 100], (255, 255, 255))
        self.full_heart = load_image("assets/ui/heart_ui/ui_heart_full.png", [50, 50], (255, 255, 255))
        self.half_heart = load_image("assets/ui/heart_ui/ui_heart_half.png", [50, 50], (255, 255, 255))
        self.empty_heart = load_image("assets/ui/heart_ui/ui_heart_empty.png", [50, 50], (255, 255, 255))

        self.heart_list = [self.full_heart for i in range(0, 3)]

    def render(self, display):
        display.blit(self.heart_frame, [0, 0])

        for i in range(50, 200, 50):
            if i == 50:
                display.blit(self.heart_list[0], [i, 30])
            if i == 100:
                display.blit(self.heart_list[1], [i, 30])
            if i == 150:
                display.blit(self.heart_list[2], [i, 30])

    def lose_life(self):
        if self.heart_list[-1] == self.full_heart:
            self.heart_list[-1] = self.half_heart

        elif self.heart_list[-1] == self.half_heart:
            self.heart_list[-1] = self.empty_heart

        elif self.heart_list[-2] == self.full_heart:
            self.heart_list[-2] = self.half_heart

        elif self.heart_list[-2] == self.half_heart:
            self.heart_list[-2] = self.empty_heart

        elif self.heart_list[-3] == self.full_heart:
            self.heart_list[-3] = self.half_heart

        elif self.heart_list[-3] == self.half_heart:
            self.heart_list[-3] = self.empty_heart


class Slot:
    def __init__(self):
        self.img = self.slot = load_image("assets/ui/slot.png", [40, 40], (255, 255, 255))
        self.item = None

    def render(self, display: pygame.Surface, x, y):
        display.blit(self.img, [x, y])

    def set_item(self, item):
        self.item = item


class HotBar:
    def __init__(self):
        self.frame = load_image("assets/ui/frame/inventory_frame.png", [200, 125], (255, 255, 255))
        self.slot = Slot()

        self.slot_list = [self.slot for i in range(0, 3)]

    def render(self, display: pygame.Surface):
        for i in range(30, 160, 50):
            self.slot.render(display, i, 621)
        display.blit(self.frame, [0, 575])
