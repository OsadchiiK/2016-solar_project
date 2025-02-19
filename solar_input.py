# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet  # planet is unused. why?
import numpy as np


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = parse_star_parameters(line)
                objects.append(star)
            elif object_type == "planet":
                planet = parse_planet_parameters(line)
                objects.append(planet)
            else:
                print("Unknown space object")
    return objects


def parse_star_parameters(line):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    line = line.split()
    raduis = float(line[1])
    color = line[2]
    mass = float(line[3])
    r = np.array([float(line[4]), float(line[5])])
    V = np.array([float(line[6]), float(line[7])])
    return Star(raduis, color, mass, r, V)


def parse_planet_parameters(line):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    line = line.split()
    raduis = float(line[1])
    color = line[2]
    mass = float(line[3])
    r = np.array([float(line[4]), float(line[5])])
    V = np.array([float(line[6]), float(line[7])])
    return Planet(raduis, color, mass, r, V)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as f:
        for obj in space_objects:
            f.write(str(obj.type) + " " +
                    str(obj.radius) + " " +
                    str(obj.color) + " " +
                    str(obj.mass) + " " +
                    str(obj.r) + " " +
                    str(obj.V) + "\n")


if __name__ == "__main__":
    print("This module is not for direct call!")
