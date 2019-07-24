# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
colors = {
        "1": dict(color=sd.COLOR_RED, name="Red"),
        "2": dict(color=sd.COLOR_ORANGE, name="Orange"),
        "3": dict(color=sd.COLOR_YELLOW, name="Yellow"),
        "4": dict(color=sd.COLOR_GREEN, name="Green"),
        "5": dict(color=sd.COLOR_CYAN,name='Cyan'),
        "6": dict(color=sd.COLOR_BLUE,name="Blue"),
        "7": dict(color=sd.COLOR_PURPLE,name="Purple"),
        "8": dict(color=sd.COLOR_DARK_YELLOW,name="Dark yellow"),
        "9": dict(color=sd.COLOR_DARK_ORANGE,name="Dark orange"),
        "10": dict(color=sd.COLOR_DARK_RED,name="Dark red"),
        "11": dict(color=sd.COLOR_DARK_GREEN,name="Dark green"),
        "12": dict(color=sd.COLOR_DARK_CYAN,name="Dark cyan"),
        "13": dict(color=sd.COLOR_DARK_BLUE,name="Dark blue"),
        "14": dict(color=sd.COLOR_DARK_PURPLE,name="Dark purple"),
        }


def draw_vector(count_angle, start_point, start_angle, lenght, color):
    angle = 360/count_angle
    local_point = start_point
    for i in range(count_angle):
        v1 = sd.get_vector(start_point=local_point, angle=start_angle + i * angle, length=lenght, width=3)
        v1.draw(color=color)
        local_point = v1.end_point
        if i == count_angle - 1:
            sd.line(local_point, start_point, color, width=3)


def triangle(point, angle, lenght, color):
    draw_vector(3, point, angle, lenght, color)


def quadrat(point, angle, lenght, color):
    draw_vector(4, point, angle, lenght, color)

def pentagon(point, angle, lenght, color):
    draw_vector(5, point, angle, lenght, color)

def gexagon(point, angle, lenght,color):
    draw_vector(6, point, angle, lenght, color)

#i = 1
#print(colors['{}'.format(i)]['name'])
for item in colors:  #
    print(item + ":" + colors[item]['name'])
    #print(item + ":" + colors['{}'.format(item)]['name'])
#    print(item + ":" + item['{}'.format(item)]['name'])



def init_vvod():
    while True:
        print("Введите номер цвета:")
        promt = input()
        if 0 > int(promt) or int(promt) > 15:
            print("Вы ввели некорректный номер цвета!")

        else:
            print("Вы выбрали:" + colors[promt]['name'])
            return promt





promt = init_vvod()
triangle_point = sd.get_point(100, 100)
triangle(triangle_point, 10, 100, colors[promt]['color'])

quad_point = sd.get_point(400, 100)
quadrat(quad_point, 10, 100, colors[promt]['color'])

pentagon_point = sd.get_point(100, 400)
pentagon(pentagon_point, 20, 100, colors[promt]['color'])

gexagon_point = sd.get_point(400, 400)
gexagon(gexagon_point, 20, 100, colors[promt]['color'])
sd.pause()
