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
        return "Вода"

    def __add__(self, other):
        if  other.content == 'воздух':
            return Storm()
        elif other.content == 'огонь':
            return Par()
        elif other.content == 'земля':
            return Graz()


class Air:
    def __init__(self):
        self.content = "воздух"

    def __str__(self):
        return "Воздух"

    def __add__(self, other):
        if other.content == 'вода':
            return Storm()
        elif other.content == 'огонь':
            return Flash()
        elif other.content == 'земля':
            return Dust()


class Fire:
    def __init__(self):
        self.content = "огонь"

    def __str__(self):
        return "Огонь"

    def __add__(self, other):
        if other.content == 'вода':
            return Par()
        elif other.content == 'земля':
            return Lawa()
        elif other.content == 'воздух':
            return Flash()


class Earth:
    def __init__(self):
        self.content = "земля"

    def __str__(self):
        return "Земля"

    def __add__(self, other):
        if other.content == 'вода':
            return Graz()
        elif other.content == 'огонь':
            return Lawa()
        elif other.content == 'воздух':
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




# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
