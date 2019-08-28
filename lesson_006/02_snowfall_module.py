# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sf
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
sf.create_snow(20)
while True:
    sd.start_drawing()
    sf.draw_snow(sd.background_color)
    sf.change_point(sd.randint(2, 20))
    sf.draw_snow(sd.COLOR_WHITE)
    final_flake = sf.check_snow()
    if len(final_flake) > 0:
        sf.delete(final_flake)
        sf.create_snow(len(final_flake))
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.finish_drawing()
    sd.sleep(0.1)

    if sd.user_want_exit():
        break

sd.pause()
