# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

#start_point = sd.get_point(50, 50)
#end_point = sd.get_point(350, 450)
#width = 50
step = 50

def draw_raibow(start_point,width):
    i = 1
    for color in rainbow_colors:
        #point = sd.get_point(420, -50)
        sd.circle(start_point, 800 + i * width, color, width)
        i += 1
    #sd.pause()
