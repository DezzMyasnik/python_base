# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.



import zipfile
from pprint import pprint
from abc import ABCMeta, abstractmethod
from collections import defaultdict

def sortByAlphabet(input_str):

    return input_str[0]

def sortByCount(input_str):

    return input_str[1]

class CharStat(metaclass=ABCMeta):

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = defaultdict(int)

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
           zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()

        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect(line)




    def _collect(self, line):
        for char in line:
            if char.isalpha():
                self.stat[char] += 1

    def prepare(self):
        print('+---------+----------+')
        print('|  буква  |  частота |')
        print('+---------+----------+')
        args_ = self._print_list()
        i =0
        for item in sorted(list(self.stat.items()), key=args_[0], reverse=args_[1]):
            i+=item[1]

            print('+   {0}     +  {1:7d} +'.format(item[0], item[1]))
        print('+---------+----------+')

        print('+   {0} +  {1:7d} +'.format("Итого",i))
        print('+---------+----------+')

    @abstractmethod
    def _print_list(self):
        pass


class Sort_1(CharStat):

    def _print_list(self):

        return (sortByAlphabet, True,)




class Sort_2(CharStat):

    def _print_list(self):
        return (sortByAlphabet, False)



class Sort_3(CharStat):

    def _print_list(self):
        return (sortByCount, False, )



class Sort_4(CharStat):

    def _print_list(self):
        return (sortByCount, True,)



print('Упорядочивание по частоте - по убыванию')
chatterer_4 = Sort_4(file_name='voyna-i-mir.txt.zip')
chatterer_4.collect()
chatterer_4.prepare()


print('по частоте по возрастанию')
chatterer_3 = Sort_3(file_name='voyna-i-mir.txt.zip')
chatterer_3.collect()
chatterer_3.prepare()

print('по алфавиту по возрастанию')
chatterer_2 = Sort_2(file_name='voyna-i-mir.txt.zip')
chatterer_2.collect()
chatterer_2.prepare()

print('по алфавиту по убыванию')
chatterer = Sort_1(file_name='voyna-i-mir.txt.zip')
chatterer.collect()
chatterer.prepare()






#out_list = sorted(chatterer.stat.items(), key=lambda x: -x[1])
#pprint(out_list)

#out_list = sorted(chatterer.stat.items(), key=lambda x: x[1])
#pprint(out_list)

#out_list = sorted(chatterer.stat.items(), key=lambda x: x[0])
#pprint(out_list)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
