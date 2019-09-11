# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
sd.set_screen_size(1200,600)

class Snowflake:
    def __init__(self):

        self.lenght = sd.random_number(10, 70)
        self.center_point = sd.get_point(sd.random_number(100, 400), sd.random_number(500, 600))

    def clear_previous_picture(self):
        sd.snowflake(center=self.center_point, length=self.lenght, color=sd.background_color)

    def move(self):
        self.center_point = sd.get_point(self.center_point.x + sd.randint(2, 10),
                                         self.center_point.y - sd.randint(2, 10))

    def draw(self):
        sd.snowflake(center=self.center_point, length=self.lenght, color=sd.COLOR_WHITE)


    def can_fall(self):
        return self.center_point.y > 0


    def __del__(self):
        self.center_point = None
        self.lenght = None


'''
flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
'''
def get_flakes(count):
    fl = []
    for i in range(count):
        one_flake = Snowflake()
        fl.append(one_flake)
    return fl   



# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=20)  # создать список снежинок

def get_fallen_flakes():
    i=0
    #list_fl = enumerate(flakes)

    for id in reversed(range(len(flakes))):
        if not flakes[id].can_fall():
            del flakes[id]
            #flakes.remove(item)
            i += 1
    return  i


def append_flakes(count):
    item = get_flakes(count)
    flakes.extend(item)


while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    #print (fallen_flakes)
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break





sd.pause()
