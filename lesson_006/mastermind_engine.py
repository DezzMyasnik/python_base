from random import randint

_holder = []
def generator_int(size):
    global _holder
    _holder = []
    for i in range(size):
        if i == 0:
            _holder.append(randint(1, 9))

        else:
            _holder.append(proverka(_holder, randint(0, 9)))

    return _holder


def proverka(list, test_int):  # TODO не правильно использовать зарезервированные слова как название переменных
    if test_int in list:
        return proverka(list, randint(0,9))  # TODO рекурсия слишком дорого, достаточно бесконечного цикла
    else:
        return test_int


def main_proverka(test_str):
    global _holder
    cow = 0
    for item in list(test_str):  # TODO зачем поборачивать в лист?
        if int(item) in _holder:  # TODO так не правильно -  сумма коров и быком не может быть больше 4,
            # то есть если бык то не корова
            cow += 1
    bull = 0
    for i in range(0, list(test_str).__len__()):  # TODO что это)? у строки тоже есть длина и есть функция len для получения
        if int(test_str[i]) == _holder[i]:
            bull += 1
    result = {
        'bulls': bull,
        'cows': cow
    }
    return result


def povtor(test_str):
    for item in list(test_str):  # TODO попробуйте использовать set для проверки
        if list(test_str).count(item) > 1:
           return True  # TODO масло масляное условие выше уже бул
        else:
            return False