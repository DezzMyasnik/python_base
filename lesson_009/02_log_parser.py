# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


import datetime
from time import strftime
from pprint import pprint


class Parser:

    def __init__(self, filename):
        self.name = filename
        self.log_val = {}
        self.log = []
        self.stata = {}

    def read_log(self):
        with open(self.name, 'r', encoding='cp1251') as file:
            for line in file:
                self.log_parese(line)
                # self.collect(line)
            self.nok_count()

    def log_parese(self, line):
        line = line.rstrip('\n')
        splitted = line.rsplit('] ')
        splitted[0] = splitted[0].lstrip('[')
        # print(splitted[0].find('.', 0, len(splitted[0])))
        splitted[0] = splitted[0][:splitted[0].find('.', 0, len(splitted[0])) - 3]
        local = [splitted[1], splitted[0]]
        self.log.append(local)

    def nok_count(self):
        for item in self.log:

            if item[0] == 'NOK':

                if item[1] in self.stata:

                    self.stata[item[1]] += 1
                else:
                    self.stata[item[1]] = 1

    def __str__(self):

        return str(list(self.stata))


test = Parser('events.txt')
test.read_log()
with open('events_res.txt', 'w') as file:
    for item in test.stata.items():
        str_out = '[{}] {}\n'.format(item[0], item[1])
        file.write(str_out)

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
