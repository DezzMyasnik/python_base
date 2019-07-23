# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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

figs= {'1': dict(name="Треугольник", fun=triangle),  # TODO функции тоже обекты, их можно помещать в словарь
       '2': dict(name='Квадрат', fun=quadrat),
       '3': dict(name="пятиугольник", fun=pentagon),
       '4': dict(name="шестиугольник", fun=gexagon)
       }

#i = 1
#print(colors['{}'.format(i)]['name'])
for item in figs:
    print(item + ":" + figs[item]['name'])


def init_vvod():
    print("Выбирете желаемую фигуру >")
    prom = input()
    if 0 < int(prom) < 5:
        print("Вы выбрали:" + figs[prom]['name'])
    else:
        print("Вы ввели некорректный номер фигуры!")
        init_vvod()
    return prom

#TODO вопрос: при первичном вводе неверного номера фигуры, выводиться сообщение о некорректном номере,
# однако после ввода корректного номера выдается ошибка о неверном номере. возвращаемое функцией init_vvod
# не перезаписывается в переменную prompt_1. туда почему то записывается первичный ввод?

promt_1 = init_vvod()
center_point = sd.get_point(sd.resolution[0]/2, sd.resolution[1]/2)
lenght = 100
angle = 10
color = sd.COLOR_YELLOW
figs[promt_1]['fun'](point=center_point, lenght=lenght, angle=angle, color=color)
#if promt == '1':
#
#elif promt == '2':
#    quadrat(point=center_point, lenght=lenght, angle=angle, color=color)
#elif promt == '3':
#    gexagon(point=center_point, lenght=lenght, angle=angle, color=color)
#else:
#   sexagon(point=center_point, lenght=lenght, angle=angle, color=color)

sd.pause()
