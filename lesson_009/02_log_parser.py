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

from abc import ABCMeta, abstractmethod
from collections import defaultdict

class Parser(metaclass=ABCMeta):

    def __init__(self, filename):
        self.name = filename
        self.log = []
        self.stata = defaultdict(int)

    def read_log(self):
        with open(self.name, 'r', encoding='cp1251') as file:
            for line in file:
                self.log_parse(line)

            self.nok_count()

    @abstractmethod
    def _get_data_str(self,data):
        pass


    def log_parse(self, line):  #
        line = line.rstrip('\n')
        splitted = line.rsplit('] ')
        splitted[0] = splitted[0].lstrip('[')
        splitted[0] = self._get_data_str(splitted[0])
        local = [splitted[1], splitted[0]]
        self.log.append(local)

    def nok_count(self):
        for item in self.log:
            if item[0] == 'NOK':
                self.stata[item[1]] += 1

    def __str__(self):
        return str(self.stata)

class MinutPareser(Parser):

    def _get_data_str(self,data):

        return data[:data.find('.', 0, len(data)) - 3]

class HourPareser(Parser):

    def _get_data_str(self,data):

        return data[:data.find('.', 0, len(data)) - 6]

class DayPareser(Parser):

    def _get_data_str(self,data):

        return data[:data.find('.', 0, len(data)) - 9]

class MounthParser(Parser):

    def _get_data_str(self,data):

        return data[:data.find('.', 0, len(data)) - 12]


class YearParser(Parser):

    def _get_data_str(self, data):

        return data[:data.find('.', 0, len(data)) - 15]


out_list =[]
test = MinutPareser('events.txt')
test.read_log()
out_list.extend(test.stata.items())
test = HourPareser('events.txt')
test.read_log()
out_list.extend(test.stata.items())
test = DayPareser('events.txt')
test.read_log()
out_list.extend(test.stata.items())
test = MounthParser('events.txt')
test.read_log()
out_list.extend(test.stata.items())
test = YearParser('events.txt')
test.read_log()
out_list.extend(test.stata.items())


with open('events_res.txt', 'w') as file:
    for item in out_list:
        str_out = '[{}] {}\n'.format(item[0], item[1])
        file.write(str_out)
#зачет!