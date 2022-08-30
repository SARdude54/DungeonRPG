import pygame

from pygame.locals import *
from .image import load_image
from .weapons import *

# Classes for widgets and ui


class HealthBar:
    def __init__(self):
        """
        Health bar ui for player.
        """
        self.heart_frame = load_image("assets/ui/frame/heart_frame.png", [250, 100], (255, 255, 255))
        self.full_heart = load_image("assets/ui/heart_ui/ui_heart_full.png", [50, 50], (255, 255, 255))
        self.half_heart = load_image("assets/ui/heart_ui/ui_heart_half.png", [50, 50], (255, 255, 255))
        self.empty_heart = load_image("assets/ui/heart_ui/ui_heart_empty.png", [50, 50], (255, 255, 255))

        self.heart_list = [self.full_heart for i in range(0, 3)]

    def render(self, display):
        """
        renders health bar
        :param display: pygame.Surface
        :return: None
        """
        display.blit(self.heart_frame, [0, 0])

        for i in range(50, 200, 50):
            if i == 50:
                display.blit(self.heart_list[0], [i, 30])
            if i == 100:
                display.blit(self.heart_list[1], [i, 30])
            if i == 150:
                display.blit(self.heart_list[2], [i, 30])

    def lose_life(self):
        """
        Replace hearts when player takes damage
        :return:
        """
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
        """
        Slot widget for inventory and hotbar. A container for game items such as weapons and potions
        """
        self.img = self.slot = load_image("assets/ui/slot.png", [40, 40], (255, 255, 255))
        self.item = None

    def render(self, display: pygame.Surface, x, y):
        """
        renders slot
        :param display: pygame.Surface
        :param x: int
        :param y: int
        :return: None
        """
        display.blit(self.img, [x, y])

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item


class HotBar:
    def __init__(self):
        """
        Hot bar ui for player
        """
        self.frame = load_image("assets/ui/frame/inventory_frame.png", [200, 125], (255, 255, 255))
        self.slot_1 = Slot()
        self.slot_2 = Slot()
        self.slot_3 = Slot()

        self.slot_list = [self.slot_1, self.slot_2, self.slot_3]

    def render(self, display: pygame.Surface):
        """
        renders hotbar
        :param display: pygame.Surface
        :return: None
        """
        for i in range(30, 160, 50):
            if i == 30:
                self.slot_1.render(display, i, 621)
            if i == 80:
                self.slot_2.render(display, i, 621)
            if i == 130:
                self.slot_3.render(display, i, 621)

        for i in range(0, 3):
            if self.get_items()[i] is not None and i == 0:
                display.blit(self.get_items()[i], [47, 627])
            if self.get_items()[i] is not None and i == 1:
                display.blit(self.get_items()[i], [97, 627])
            if self.get_items()[i] is not None and i == 2:
                display.blit(self.get_items()[i], [147, 627])

        display.blit(self.frame, [0, 575])

    def add_item(self, item: pygame.Surface):
        """
        adds an item to the hotbar
        :param item: pygame.Surface
        :return: None
        """
        if self.slot_1.get_item() is None:
            self.slot_1.set_item(item)
        elif self.slot_1.get_item() is not None and self.slot_2.get_item() is None:
            self.slot_2.set_item(item)
        elif self.slot_1.get_item() is not None and self.slot_2.get_item() is not None and self.slot_3.get_item() is None:
            self.slot_3.set_item(item)

    def get_items(self):
        return [self.slot_list[i].get_item() for i in range(0, 3)]

