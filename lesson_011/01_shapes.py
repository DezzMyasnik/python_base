# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.



def get_polygon(n):

    def draw_vector(point, angle, length):
        corner = 360 / n
        local_point = point
        for i in range(n):
            v1 = sd.get_vector(start_point=local_point, angle=angle + i * corner, length=length, width=3)
            v1.draw()
            local_point = v1.end_point
            if i == n - 1:
                sd.line(local_point, point, sd.COLOR_YELLOW, width=3)

    return draw_vector


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=200)


sd.pause()
#зачет!