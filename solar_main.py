# coding: utf-8
# license: GPLv3

import pygame
import time
from solar_vis import *
from solar_model import *
from solar_input import *
from solar_objects import *
import thorpy

import numpy as np


finished = False

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта"""

time_scale = 100
"""Шаг по времени при моделировании"""

space_objects = []
"""Список космических объектов."""


def execution(dt):
    """Функция исполнения -- выполняется циклически,
    вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от
    значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает
    вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global physical_time
    recalculate_space_objects_positions(space_objects, dt)
    physical_time += dt


def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True


def pause_execution():
    global perform_execution
    perform_execution = False


def open_file():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    in_filename = "solar_system.txt"
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.r[0]), abs(obj.r[1])) for obj in space_objects])
    calculate_scale_factor(max_distance)


def events(events, menu):
    global finished
    for event in events:
        menu.react(event)
        if event.type == pygame.QUIT:
            finished = True


def slider_to_real(val):
    return np.exp(6.5 + val)


def slider_reaction(event):
    global time_scale
    time_scale = slider_to_real(event.el.get_value())


def init_ui():
    slider = thorpy.SliderX(50, (0, 10), "Simulation speed")
    button_load = thorpy.make_button("Load a file", func=open_file)
    button_pause = thorpy.make_button("Pause", func=pause_execution)
    button_play = thorpy.make_button("Play", func=start_execution)
    box = thorpy.Box(elements=[
        slider,
        button_play,
        button_pause,
        button_load
        ])
    reaction1 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=slider_reaction,
                                event_args={"id": thorpy.constants.EVENT_SLIDE}
                                )
    box.add_reaction(reaction1)
    menu = thorpy.Menu(box)
    box.set_topleft((0, 680))
    box.blit()
    box.update()
    return menu, box


def main():
    global physical_time
    global perform_execution
    print('Modelling started!')
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    last_time = time.perf_counter()
    drawer = Drawer(screen)
    menu, box = init_ui()
    perform_execution = True

    while not finished:
        events(pygame.event.get(), menu)
        current_time = time.perf_counter()
        if perform_execution:
            execution((current_time - last_time) * time_scale)
        last_time = current_time
        drawer.update(space_objects, box)

    print('Modelling finished!')


if __name__ == "__main__":
    main()
