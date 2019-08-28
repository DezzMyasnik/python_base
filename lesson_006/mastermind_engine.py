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


def proverka(input_arr, test_int):
    while test_int in input_arr:
             test_int = randint(0,9)


    return test_int


def main_proverka(test_str):
    global _holder
    cow = 0
    #for item in test_str:
    #    if int(item) in _holder:
    #        # то есть если бык то не корова
    #        cow += 1
    # сумма не сможет быть больше 4 так как до этого происходить проверка на длину строки вводимой пользователем
    bull = 0
    for i in range(0, len(test_str)):
        if int(test_str[i]) in _holder:
            cow += 1
        if int(test_str[i]) == _holder[i]:
            bull += 1
    result = {
        'bulls': bull,
        'cows': cow
    }
    return result


def povtor(test_str):
    return len(set(test_str)) == 4
