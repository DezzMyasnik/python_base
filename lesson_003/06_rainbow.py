# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

start_point = sd.get_point(50, 50)
end_point = sd.get_point(350, 450)
width = 50
step = 50
#i = 1
#for color in rainbow_colors:
##    new_point_sart = sd.get_point(start_point.x + i*step, start_point.y)
#    new_point_end = sd.get_point(end_point.x + i * step, end_point.y)
#    sd.line(new_point_sart, new_point_end, color, width)
#    i += 1
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

i = 1
for color in rainbow_colors:
    point=sd.get_point(420, -50)
    sd.circle(point, 300 + i * step, color, width)
    i += 1
sd.pause()
