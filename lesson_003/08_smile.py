# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.



def smile_draw(x_coord, y_coord, color):
    center_point = simple_draw.get_point(x_coord,y_coord)
    simple_draw.circle(center_position=center_point, radius=30, color=color, width=2)
    left_eye_sp = simple_draw.get_point(center_point.x - 15, center_point.y + 10)
    left_eye_ep = simple_draw.get_point(center_point.x - 5, center_point.y + 10)
    simple_draw.line(left_eye_sp, left_eye_ep, color, width=2)
    right_eye_sp = simple_draw.get_point(center_point.x + 15, center_point.y + 10)
    right_eye_ep = simple_draw.get_point(center_point.x + 5, center_point.y + 10)
    simple_draw.line(right_eye_sp, right_eye_ep, color, width=2)
    mouth_sp = simple_draw.get_point(center_point.x - 10, center_point.y - 10)
    mouth_ep = simple_draw.get_point(center_point.x + 10, center_point.y - 10)
    simple_draw.line(mouth_sp, mouth_ep, color, width=2)


for i in range(10):
    point = simple_draw.random_point()
    smile_draw(point.x, point.y, simple_draw.COLOR_YELLOW)

simple_draw.pause()
#зачет!