# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.number = get_prime_numbers(n)


    def __iter__(self):

        self.i = 0
        # возвращаем ссылку на себя - я буду итератором!
        return self


    def __next__(self):

        try:
            item = self.number[self.i]
            self.i += 1
            return item


        except IndexError as exc:

            raise StopIteration()







prime_number_iterator = PrimeNumbers(n=100000)
for number in prime_number_iterator:
    print(number)


# TODO после подтверждения части 1 преподователем, можно делать
'''


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            yield number
            prime_numbers.append(number)


def filter_one(n):
    dlina_chisla = len(str(n))

    if len(str(n)) % 2 == 0:
        second = str(n)[int((dlina_chisla / 2)):]
    else:
        second = str(n)[int((dlina_chisla / 2)) + 1:]
    first = str(n)[0:int(dlina_chisla / 2)]
    first_part, second_part = 0, 0
    for noun in first:
        first_part += int(noun)
    for noun in second:
        second_part += int(noun)
    if first_part is second_part:
          return True

def polyndrome(n):
    strdd = str(n)[::-1];
    if str(n) == strdd:
        return True

for number in prime_numbers_generator(n=100000):
    # filter_one(number)
    if filter_one(number):
       print(f"{number} {filter_one(number)}")
    #print('Полиндромы')
    if polyndrome(number):
        print(f"{number} {polyndrome(number)}")
# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
'''