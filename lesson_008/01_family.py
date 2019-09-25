 # -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint
coat = 0  # TODO посмотрите на python_snippets/07_practice.py. Там счетчики хранятся в классах
total_money = 0
total_eat = 0
######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dust  = 0

    def __str__(self):
        return "В доме денег - {}, еды - {}, грязи - {}".format(self.money,self.food, self.dust)

    def add_dust(self):
        self.dust += 5




class Man:  # TODO Man - это мужчина, не лучшее название для базового класса

    def __init__(self,name):
        self.name = name
        self.happyness = 100
        self.fullness = 30
        self.house = None

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')


    def __str__(self):
        return '{}, сытость {}, {} счастья'.format(
            self.name, self.fullness, self.happyness)

    def check_dust(self):
        if self.house.dust >=90:
            self.happyness -= 10



class Husband(Man):

    def __str__(self):  # TODO зачем тогда?
        return super().__str__()

    def act(self):
        self.check_dust()
        if self.fullness <= 0 or self.happyness <= 10:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)

        if self.fullness <= 30:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.gaming()

    def eat(self):  # TODO это логика базового класса
        global  total_eat
        if self.house.food >= 30:  # min(30, self.house.food )
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
            total_eat += 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')


    def work(self):
        global total_money
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.fullness -=10
        self.house.money +=150
        total_money += 150

    def gaming(self):
        cprint('{} поиграл в WOT'.format(self.name), color='blue')
        self.fullness -= 10
        self.happyness += 20



class Wife(Man):


    def __str__(self):
        return super().__str__()

    def go_to_the_house(self, house):  # TODO это метод базовго класса
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехала в дом'.format(self.name), color='cyan')


    def act(self):
        self.check_dust()  # TODO сначало лучше проверить на живость
        if self.fullness <= 0 or self.happyness <= 10:
            cprint('{} умерла...'.format(self.name), color='red')
            return
        dice = randint(1, 4)

        if self.house.food <= 30:
            self.shopping()
        elif self.fullness <= 30:
            self.eat()

        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.buy_fur_coat()
        elif dice == 4:
            self.clean_house()

    def eat(self):
        global total_eat
        if self.house.food >= 30:
            cprint('{} поела'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
            total_eat += 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        global coat
        if self.house.money > 360:
            cprint('{} сходила в магазин за шубой'.format(self.name), color='magenta')
            self.happyness += 90  # TODO 90?
            self.house.money -= 360
            self.fullness -= 10
            coat += 1

    def clean_house(self):
        cprint('{} прибралась в доме'.format(self.name), color='magenta')
        self.fullness -= 10
        if self.house.dust >= 100:  # TODO просто min(100 и текущий уровень грязи)

            self.house.dust -= 100
        else:
            self.house.dust = 0


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
serge.go_to_the_house(home)
masha.go_to_the_house(home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.add_dust()
    serge.act()
    masha.act()

    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

cprint('Заработано денег - {}, куплено шуб - {}, съедено еды - {}'.format(
    total_money, coat, total_eat
), color='red')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

