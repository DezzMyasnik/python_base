# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# TODO здесь ваш код

from abc import ABCMeta, abstractmethod
from collections import defaultdict


class Parser(metaclass=ABCMeta):

    def __init__(self, filename):
        self.name = filename
        self.log = []
        self.stata = defaultdict(int)
        self.read_log()

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):

        try:

            d = list(self.stata.keys())
            returnedval = (d[self.i], self.stata[d[self.i]])
            self.i += 1
            return returnedval

        except IndexError as exc:
            raise StopIteration()

    def read_log(self):
        with open(self.name, 'r', encoding='cp1251') as file:
            for line in file:
                self.log_parse(line)

            self.nok_count()

    @abstractmethod
    def _get_data_str(self, data):
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


class MinutPareser(Parser):

    def _get_data_str(self, data):
        return data[:data.find('.', 0, len(data)) - 3]


grouped_events = MinutPareser('events.txt')

# test.read_log()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
#зачет!