# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


from numpy import random

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass

class DrunkError(Exception):
    pass





def one_day():

    try:
         ob = random.choice([IamGodError('Я есть божество'),
                             DrunkError("Напился"),
                             CarCrashError("Разбил машину"),
                             GluttonyError("Обожрался"),
                             DepressionError("Стрессанул"),
                             SuicideError("Самоубился"), BaseException()],
                             size=1,
                             p=[1/13,1/13,1/13, 1/13, 1/13, 1/13,7/13])

         raise ob[0]
    except (IamGodError, DrunkError, CarCrashError,GluttonyError,DepressionError,SuicideError, BaseException) as exc:
        with open('log.txt', 'a', encoding='utf-8') as file:
            if type(exc) is not BaseException:
                file.writelines(f'Поймано исключение {exc} \n')
            else:
                file.writelines(f'Поймано базовое исключение \n')


    return random.randint(1, 7)
"""
        raise IamGodError('Я есть божество')
        raise DrunkError("Напился")
        raise CarCrashError("Разбил машину")
        raise GluttonyError("Обожрался")
        raise DepressionError ("Стрессанул")
        raise SuicideError("Самоубился")"""



i=0
while i <= ENLIGHTENMENT_CARMA_LEVEL:
    i += one_day()
    print(i)

# https://goo.gl/JnsDqu
