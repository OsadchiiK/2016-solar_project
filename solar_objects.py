# coding: utf-8
# license: GPLv3
import pygame


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self, radius, color, mass, r, V):
        self.radius = radius
        self.color = color
        self.mass = mass
        self.r = r
        self.V = V
        self.F = 0
        self.image = None
        self.type = "star"

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            self.r,
            self.radius
        )


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, radius, color, mass, r, V):
        self.radius = radius
        self.color = color
        self.mass = mass
        self.r = r
        self.V = V
        self.F = 0
        self.image = None
        self.type = "planet"

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            self.r,
            self.radius
        )
