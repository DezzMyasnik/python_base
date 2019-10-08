 # -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint
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
        self.dust = 0
        self.cats_eat = 30

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {},  кошачей еды - {}, грязи - {}'.format(
                self.food, self.money, self.cats_eat, self.dust)


    def add_dust(self):
        self.dust += 5




class Human:
    total_eat = 0
    def __init__(self,name):
        self.name = name
        self.happyness = 100
        self.fullness = 30
        self.house = None

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        if type(self) is Wife:
            cprint('{} въехала в дом '.format(self.name), color='yellow')
        else:
            cprint('{} въехал в дом'.format(self.name), color='yellow')

    def eat(self):
        if self.house.food >= 30:  # min(30, self.house.food )
            if type(self) is Wife:
                cprint('{} поела'.format(self.name), color='yellow')
            else:
                cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
            Human.total_eat += 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def __str__(self):
        return '{}, сытость {}, {} счастья'.format(
            self.name, self.fullness, self.happyness)

    def check_dust(self):
        if self.house.dust >= 90:
            self.happyness -= 10

    def get_cat(self, cat):
        cat.house = self.house
        cprint('{} подобрал кота {}'.format(self.name, cat.name))

    def pet_the_cat(self):
        self.happyness += 5
        if type(self) is Wife:
            cprint('{} погладила кота'.format(self.name))
        else:
            cprint('{} погладил кота'.format(self.name), color='yellow')

    def buy_cats_eat(self):
        self.fullness -= 10
        if self.house.money >= 10:

            if type(self) is Wife:
                cprint('{} сходила в магазин за кошачей едой'.format(self.name), color='magenta')

            else:
                cprint('{} сходил в магазин за кошачей едой'.format(self.name), color='magenta')

            self.house.cats_eat += 10
            self.house.money -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')


class Husband(Human):
    total_money = 0


    def act(self):
        self.check_dust()
        if self.fullness <= 0 or self.happyness <= 10:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)

        if self.fullness <= 30:
            self.eat()
        elif self.house.cats_eat <= 10:
            if self.house.money <=10:
                self.work()
            else:
                self.buy_cats_eat()
        elif self.house.money <= 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.gaming()
        elif dice == 4:
            self.pet_the_cat()


    def work(self):

        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.fullness -=10
        self.house.money +=150
        Husband.total_money += 150

    def gaming(self):
        cprint('{} поиграл в WOT'.format(self.name), color='blue')
        self.fullness -= 10
        self.happyness += 20



class Wife(Human):
    coat = 0

    def act(self):
        if self.fullness <= 0 or self.happyness < 10:
            cprint('{} умерла...'.format(self.name), color='red')
            return

        self.check_dust()
        dice = randint(1, 5)

        if self.fullness <= 30:
            if self.house.food <=30:
                self.shopping()
                self.eat()
            else:
                self.eat()

        elif self.house.food <= 30:
            self.shopping()
        elif self.house.cats_eat <= 10:
            self.buy_cats_eat()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.buy_fur_coat()
        elif dice == 4:
            self.clean_house()
        elif dice == 5:
            Human.pet_the_cat(self)
        elif dice == 6:
            self.buy_cats_eat()

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50


        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')




    def buy_fur_coat(self):

        if self.house.money > 360:
            cprint('{} сходила в магазин за шубой'.format(self.name), color='magenta')
            self.happyness += 60
            self.house.money -= 360
            self.fullness -= 10
            Wife.coat += 1


    def clean_house(self):
        cprint('{} прибралась в доме'.format(self.name), color='magenta')
        self.fullness -= 10
        self.house.dust = self.house.dust - min(100, self.house.dust)


""""
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
    Husband.total_money, Wife.coat, Human.total_eat
), color='red')
"""
#зачет!

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

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(
            self.name, self.fullness, )

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        elif self.house.cats_eat < 10:
            self.soil()
        elif dice == 1:
            self.soil()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.cats_eat < 10:
            self.fullness -= 10
            cprint('В доме нет еды, {} не поел'.format(self.name), color='red')

            return

        else:
            self.fullness += 20
            self.house.cats_eat -= 10
            cprint('Котэ {} поел'.format(self.name), color='yellow')

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал...'.format(self.name), color='yellow')


    def soil(self):
        self.fullness -= 10
        self.house.dust += 5
        cprint('Котэ {} подрал обои'.format(self.name), color='yellow')

#home = House()
#serge = Husband(name='Сережа')
#masha = Wife(name='Маша')
#serge.go_to_the_house(home)
#masha.go_to_the_house(home)
#cat = Cat(name='Шерстяной')
#serge.get_cat(cat)

#for day in range(365):
#    cprint('================== День {} =================='.format(day), color='red')
#    home.add_dust()
#    serge.act()
#    masha.act()
#    cat.act()
#    cprint(serge, color='cyan')
#    cprint(masha, color='cyan')
#    cprint(cat, color='grey')
#    cprint(home, color='cyan')

cprint('Заработано денег - {}, куплено шуб - {}, съедено еды - {}'.format(
    Husband.total_money, Wife.coat, Human.total_eat
), color='red')
#зачет!
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

class Child(Human):

    def act(self):
        if self.fullness <= 0 :
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1,2)
        if self.fullness <= 10:
            self.eat()

        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
    def eat(self):

        if self.house.food>=10:
            self.fullness += 10
            self.house.food -= 10
            cprint('{} поел...'.format(self.name), color='magenta')

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='magenta')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
serge.go_to_the_house(home)
masha.go_to_the_house(home)
kolya.go_to_the_house(home)
serge.get_cat(murzik)
for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.add_dust()
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

cprint('Заработано денег - {}, куплено шуб - {}, съедено еды - {}'.format(
    Husband.total_money, Wife.coat, Human.total_eat
), color='red')
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

#зачет!