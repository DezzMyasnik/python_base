# -*- coding: utf-8 -*-

import simple_draw as sd

#sd.set_screen_size(1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные



# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
def sugrob(start_point, max_length):
    list = []
    N = 20
    for i in range(N):
        local = [sd.random_number(start_point.x - 30, start_point.x + 20),
                 sd.random_number(start_point.y - 40, start_point.y + 20)]
        list.append(local)

    for item in list:
        lenght = sd.random_number(10, max_length)
        point = sd.get_point(item[1], item[0])

        sd.snowflake(center=point, length=lenght, color=sd.COLOR_WHITE)

def snowfall():
    list = []
    N = 20
    for i in range(N):
        local = [sd.random_number(400, 600), sd.random_number(100, 300)]
        list.append(local)


    while True:

        #sd.clear_screen()
        lenght = sd.random_number(10, 70)
        for item in list:
            sd.start_drawing()
            point = sd.get_point(item[1], item[0])

            sd.snowflake(center=point, length=lenght, color=sd.background_color)

            item[0] -= sd.random_number(-20, 50)
            if item[0] < 50:
                point = sd.get_point(item[1], item[0])
                sd.snowflake(center=point, length=lenght, color=sd.COLOR_WHITE)

            item[1] = item[1] + sd.random_number(1, 50)
            point = sd.get_point(item[1], item[0])
            sd.snowflake(center=point, length=lenght, color=sd.COLOR_WHITE)

            sd.finish_drawing()
            sd.sleep(0.01)

        if sd.user_want_exit():
            break

    sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


#зачет!