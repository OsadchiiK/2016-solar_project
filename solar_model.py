# coding: utf-8
# license: GPLv3
import numpy as np

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.F = np.zeros(2)
    M = body.mass
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        for planet in space_objects:
            displacement = planet.r - body.r
            m = planet.mass
            distance = np.linalg.norm(displacement)
            body.F += (M*m / distance**3) * displacement


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    a = body.F/body.m
    body.r += body.V * dt  # FIXME: не понимаю как менять...
    body.V += a*dt
    # FIXME: not done recalculation of y coordinate!


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
