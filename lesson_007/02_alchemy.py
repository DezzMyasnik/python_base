# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __init__(self):
        self.content = "вода"

    def __str__(self):
        return self.content

    def __add__(self, other):
        if  type(other) is Air:
            return Storm()
        elif type(other) is Fire:
            return Par()
        elif type(other) is Earth:
            return Graz()


class Air:
    def __init__(self):
        self.content = "воздух"

    def __str__(self):
        return self.content

    def __add__(self, other):
        if type(other) is Water:
            return Storm()
        elif type(other) is Fire:
            return Flash()
        elif type(other) is Earth:
            return Dust()


class Fire:
    def __init__(self):
        self.content = "огонь"

    def __str__(self):
        return self.content

    def __add__(self, other):
        if type(other) is Water:
            return Par()
        elif type(other) is Earth:
            return Lawa()
        elif type(other) is Air:
            return Flash()


class Earth:
    def __init__(self):
        self.content = "земля"

    def __str__(self):
        return self.content

    def __add__(self, other):
        if type(other) is Water:
            return Graz()
        elif type(other) is Fire:
            return Lawa()
        elif type(other) is Air:
            return Dust()


class Storm:
    def __str__(self):
        return "Шторм"

class Par:
    def __str__(self):
        return "Пар"

class Graz:
    def __str__(self):
        return "Грязь"
class Dust:
    def __str__(self):
        return "Пыль"

class Lawa:
    def __str__(self):
        return "Лава"
class Flash:
    def __str__(self):
        return "Молния"

print(Water(), "+", Air(), "=", Air() + Water())
print(Water(), "+", Fire(), "=", Water() + Fire())
print(Water(), "+", Earth(), "=", Water() + Earth())

print(Air(), "+", Fire(), "=", Air() + Fire())
print(Air(), "+", Earth(), "=", Air() + Earth())
print(Fire(), "+", Earth(), "=", Fire() + Earth())

print(Earth(), "+", Earth(), "=", Earth() + Earth())

#зачет!


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
