# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


def draw_branches(start_point, start_angle, start_length):
    if start_length < 10:
        return
    #v_root = sd.get_vector(start_point, 90, 0.3 * start_length, width=3)
    #v_root.draw()
    rand_angle = sd.random_number(30, 30 + int(0.4 * 30))
    for i in range(-1 * rand_angle, rand_angle+1, rand_angle * 2):
        vi_angle = start_angle + i
        v1 = sd.get_vector(start_point=start_point, angle=vi_angle, length=start_length, width=3)
        v1.draw(sd.random_color())
        length = sd.random_number(75, 75 + int(0.2 * 75 )) * 0.01
        draw_branches(start_point=v1.end_point,start_angle=vi_angle, start_length= length * start_length)
    #v2_angle = start_angle - 30
    #v2 = sd.get_vector(start_point=start_point, angle=v2_angle, length=start_length, width=3)
    #v1.draw()

sd.set_screen_size(1200,600)
point_0 = sd.get_point(600, 30)
v1 = sd.get_vector(point_0, 270, 30, 3)
v1.draw()
draw_branches(point_0, 90, 100)
# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
#sd.random_number()

sd.pause()


