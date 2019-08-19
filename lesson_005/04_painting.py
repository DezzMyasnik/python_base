# -*- coding: utf-8 -*-

# Создать пакет, в котором собрать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Каждую функцию разместить в своем модуле. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from drawing import (wall, rainbow,
                     fractal, smile,
                    snowfall)

sd.set_screen_size(1200, 600)

#sd.line(sd.get_point(0, 25), sd.get_point(1200, 25), sd.COLOR_DARK_YELLOW, 50)
rainbow.draw_raibow(sd.get_point(300,60), 30)

sd.rectangle(sd.get_point(0,0), sd.get_point(1200, 50), sd.COLOR_DARK_YELLOW,0)
#temp = sd._to_screen_rect(sd.get_point(30,50),sd.get_point(200, 200))

sd.rectangle(sd.get_point(100,50), sd.get_point(450, 300), sd.COLOR_DARK_ORANGE,2)
wall.drawwall(sd.get_point(150,50), sd.get_point(400, 300))
sd.rectangle(sd.get_point(225,150), sd.get_point(325,250),sd.COLOR_DARK_BLUE,0)
sd.rectangle(sd.get_point(225,150), sd.get_point(325,250),sd.COLOR_DARK_ORANGE,2)
smile.smile_draw(275,200,sd.COLOR_YELLOW)
wall.triangle(sd.get_point(80,300), 0, 380, sd.COLOR_DARK_RED)
tree_point = sd.get_point(630, 100)

fractal.draw_tree(tree_point, 50)
tree_point = sd.get_point(780, 90)
fractal.draw_tree(tree_point, 50)
tree_point = sd.get_point(730, 70)
fractal.draw_tree(tree_point, 40)
snowfall.sugrob(sd.get_point(80, 65), 20)
smile.sun(sd.get_point(150,500))
sd.pause()
#зачет!

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
