# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint
from practice import Man, House
# Доработать практическую часть урока lesson_007/python_snippets/practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня
class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытость {}, кошачей еды - {}, грязи - {}'.format(
            self.name, self.fullness, self.house.cats_eat, self.house.dust)

    def cat_sleep(self):
        self.fullness -= 10
        cprint('{} поспал...'.format(self.name), color='yellow')
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return

    def cat_eat(self):

        if self.house.cats_eat <= 0:
            self.fullness -= 10
            cprint('В доме нет еды, {} не поел'.format(self.name), color='red')

            return

        else:
            self.fullness += 20
            self.house.cats_eat -= 10
            cprint('Котэ {} поел'.format(self.name), color='yellow')

    def cat_damadge(self):
        self.fullness -= 10
        self.house.dust += 5
        cprint('Котэ {} подрал обои'.format(self.name), color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.cat_eat()
        elif self.house.cats_eat < 10:
            self.cat_damadge()
        elif dice == 1:
            self.cat_damadge()
        elif dice == 2:
            self.cat_eat()
        else:
            self.cat_sleep()
# Человеку и коту надо вместе прожить 365 дней.

man = Man(name='Батхед')
home = House()
cat = Cat(name='Барсик')

man.go_to_the_house(house=home)
man.get_cat(cat)
home.cats_eat = 50
home.dust = 0
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    man.act()


    cat.act()
    print('--- в конце дня ---')
    print(man)
    print(cat)
    print(home)

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
