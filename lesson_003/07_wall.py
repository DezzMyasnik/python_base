# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for



for x in range(0,600, 100):
    for y in range(0, 1500, 50):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(100 + x, 50 + y)
        if y % 100 != 0:
            left_bottom.x -= 50
            right_top.x -= 50
        sd.rectangle(left_bottom, right_top, sd.COLOR_DARK_YELLOW, 2)

sd.pause()
#зачет!