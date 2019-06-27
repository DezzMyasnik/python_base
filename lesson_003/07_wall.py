# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for



for x in range(15):
    for y in range(15):
        left_bottom = sd.get_point(0 + x * 100, 0 + y * 50)
        right_top = sd.get_point(100 + x * 100, 50 + y * 50)
        if y % 2 != 0:
            left_bottom.x -= 50
            right_top.x -= 50
        sd.rectangle(left_bottom, right_top, sd.COLOR_DARK_YELLOW, 2)

sd.pause()
