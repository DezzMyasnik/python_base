# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from district.central_street.house1 import room1 as room11, room2 as room22
from district.central_street.house2 import room1, room2
#from district.soviet_street import house1, house2

#first = room1.folks
#second = room2.folks
#print(second+first)
#print(room2.folks.extend(room1.folks))
print("На районе живут: {}".format(", ".join(room11.folks +
                                            room22.folks +
                                            room1.folks +
                                            room2.folks)))



