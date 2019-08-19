# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
import pygame
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


def drawwall(start_point, end_point):
    for x in range(start_point.x, end_point.x, 100):
        for y in range(start_point.y, end_point.y, 50):
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(100 + x, 50 + y)
            if y % 100 != 0:
                left_bottom.x -= 50
                right_top.x -= 50
            sd.rectangle(left_bottom, right_top, sd.COLOR_DARK_ORANGE, 2)

    #sd.pause()
#зачет!

def draw_vector(count_angle, start_point, start_angle, lenght, color):
    #angle = 360/count_angle
    local_point = start_point
    for i in range(count_angle):
        if i == 0:
            angle = 0
            lenght = 410
        if i == 1:
            angle = 160
            lenght = 220

        if i == count_angle - 1:
            angle = 200
            lenght = 220
            #sd.line(local_point, start_point, color, width=1)

        v1 = sd.get_vector(start_point=local_point, angle=start_angle + angle, length=lenght, width=1)
        v1.draw(color=color)
        local_point = v1.end_point
        if i == count_angle - 1:
            sd.line(local_point, start_point, color, width=1)


def triangle(point, angle, lenght, color):
    point_list = [point,
                  sd.get_point(point.x+410, point.y),
                  sd.get_point(point.x+205, point.y+50)]
    sd.polygon(point_list, color, width=0)
    #draw_vector(3, point, angle, lenght, color)