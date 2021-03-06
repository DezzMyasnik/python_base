# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
"""""
def triangle(point, angle, lenght):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=lenght, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=lenght, width=3)
    v3.draw()

def quadrat(point, angle, lenght):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=lenght, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=lenght, width=3)

    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=lenght, width=3)

    v4.draw()


def gexagon(point, angle, lenght):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=lenght, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=lenght, width=3)

    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=lenght, width=3)

    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=lenght, width=3)

    v5.draw()

def sexagon(point, angle, lenght):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=lenght, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=lenght, width=3)

    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=lenght, width=3)

    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=lenght, width=3)

    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=lenght, width=3)

    v6.draw()


triangle_point = sd.get_point(100, 100)

triangle(triangle_point, 10, 100)

quadrat_point = sd.get_point(400, 100)

quadrat(quadrat_point, 0, 100)

gexagon_point = sd.get_point(100, 400)
gexagon(gexagon_point, 0, 100)

sexagon_point = sd.get_point(400, 400)
sexagon(sexagon_point, 0, 100)
"""
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?
# даже При изменении типа линии, придется преписыать все. Либо переопределять отрисовку вектора
# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def draw_vector(count_angle, start_point, start_angle, lenght):
    angle = 360/count_angle
    local_point = start_point
    for i in range(count_angle):
        v1 = sd.get_vector(start_point=local_point, angle=start_angle + i * angle, length=lenght, width=3)
        v1.draw()
        local_point = v1.end_point
        if i == count_angle - 1:
            sd.line(local_point, start_point, sd.COLOR_YELLOW, width=3)





def triangle(point, angle, lenght):
    draw_vector(3, point, angle, lenght)


def quadrat(point, angle, lenght):
    draw_vector(4, point, angle, lenght)


def gexagon(point, angle, lenght):
    draw_vector(5, point, angle, lenght)

def sexagon(point, angle, lenght):
    draw_vector(6, point, angle, lenght)

triangle_point = sd.get_point(100, 100)
triangle(triangle_point, 10, 100)

quad_point = sd.get_point(400, 100)
quadrat(quad_point, 10, 100)

gexagon_point = sd.get_point(100, 400)
gexagon(gexagon_point, 200, 100)

sexagon_point = sd.get_point(400, 400)
sexagon(sexagon_point, 20, 100)
sd.pause()
#зачет!