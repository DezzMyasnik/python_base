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

def gexagon(point, angle, lenght, color):
    draw_vector(5, point, angle, lenght, color)

def sexagon(point, angle, lenght,color):
    draw_vector(6, point, angle, lenght, color)

figs= {'1': dict(name="Треугольник"),  # TODO функции тоже обекты, их можно помещать в словарь
       '2': dict(name='Квадрат'),
       '3': dict(name="пятиугольник"),
       '4': dict(name="шестиугольник")
       }

#i = 1
#print(colors['{}'.format(i)]['name'])
for item in figs:
    print(str(item) + ":" + figs[str(item)]['name'])  # TODO см. задание 2
#    print(item + ":" + item['{}'.format(item)]['name'])

# TODO здесь ваш код


def init_vvod():
    print("Выбирете желаемую фигуру >")
    promt = input()
    if 0 > int(promt) or int(promt) > 4:
        print("Вы ввели некорректный номер фигуры!")
        init_vvod()
    else:
        print("Вы выбрали:" + figs[str(promt)]['name'])

    return promt


promt = init_vvod()

center_point = sd.get_point(sd.resolution[0]/2, sd.resolution[1]/2)
lenght = 100
angle = 10
color = sd.COLOR_YELLOW
if promt == '1':
    triangle(point=center_point, lenght=lenght, angle=angle, color=color)
elif promt == '2':
    quadrat(point=center_point, lenght=lenght, angle=angle, color=color)
elif promt == '3':
    gexagon(point=center_point, lenght=lenght, angle=angle, color=color)
else:
    sexagon(point=center_point, lenght=lenght, angle=angle, color=color)

sd.pause()
