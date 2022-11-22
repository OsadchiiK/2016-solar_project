# coding: utf-8
# license: GPLv3

import pygame
from pygame.draw import *
import numpy as np

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране, принимают
физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим.

Тип: float

Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной
характерной длине"""
    global scale_factor
    scale_factor = 0.4*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_r(rad_v):
    r = rad_v.copy()
    r *= scale_factor
    r *= np.array([1, -1])
    r += np.array([window_width//2, window_height//2])
    return r.astype("int64")


if __name__ == "__main__":
    print("This module is not for direct call!")


class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def update(self, figures, ui):
        self.screen.fill((0, 0, 0))
        for figure in figures:
            DrawObject(figure).draw(self.screen)
        ui.blit()
        ui.update()
        pygame.display.update()


class DrawObject:
    def __init__(self, obj):
        self.obj = obj

    def draw(self, surface):
        object_ = self.obj
        circle(
            surface,
            object_.color,
            tuple(scale_r(object_.r)),
            object_.radius)
