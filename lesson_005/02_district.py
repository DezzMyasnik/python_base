# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from district.central_street.house1 import room1 as room11, room2 as room22
from district.central_street.house2 import room1, room2  # TODO забыли с советской улице
from district.soviet_street.house1 import room1 as s_room1, room2 as s_room2
from district.soviet_street.house2 import room1 as s_room12, room2 as s_room22

#
print("На районе живут: {}".format(", \n".join(room11.folks +
                                            room22.folks +
                                            room1.folks +
                                            room2.folks +
                                            s_room1.folks +
                                            s_room2.folks +
                                            s_room12.folks +
                                            s_room22.folks)))


print("На Центральной улице живут: {}".format(", ".join(room11.folks +
                                            room22.folks +
                                            room1.folks +
                                            room2.folks
                                            )))
print("На Советской улице живут: {}".format(", ".join(s_room1.folks +
                                            s_room2.folks +
                                            s_room12.folks +
                                            s_room22.folks
                                            )))
