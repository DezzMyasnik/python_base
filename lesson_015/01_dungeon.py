# -*- coding: utf-8 -*-

import datetime
# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import json
import re
from decimal import *
import csv

remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']

current_exp = 0
current_location = ''
current_date = datetime.datetime.now()

# TODO Через функции это конечно можно всё реализовать, но местами это выходит неудобно и сложно.
# TODO Давайте попробуем сгруппировать это всё по классам:
# TODO Создайте три класса - Карта, Герой, Игра
# TODO К карте отнесите методы - загрузка карты, смена локации и анализ локации
# TODO К герою методы получения опыта и учет затраченного времени (можно сделать что-то вроде is_alive() метода
# TODO который вернет True, если герой ещё жив (осталось времени больше 0))
# TODO Игра же будет инициализировать объекты других классов и запускать их методы
# TODO + собирать указания пользователя и вызывать выбранные им методы
# TODO ВАЖНО! Каждый ввод пользователя проверять!
# TODO + нужен метод записи в csv. Это по своему усмотрению уже добавьте в любой из классов

def parse_location(item):
    pattern = r'Location_(B\d+|\d+)_tm(\d*\.\d+|\d+)'
    matched = re.search(pattern, item)
    if matched:
        num = matched[1]
        tm = matched[2]
        return num, tm
    else:
        return None


def get_time_delta(current_time):
    delta = datetime.datetime.now() - current_time
    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'


def atack_monster(item):
    pattern = r'[MobBs\d]_exp(\d+)_tm(\d+){1,15}'
    matched = re.search(pattern, item)
    exp = matched[1]
    tm = matched[2]
    return exp, tm


def hatch_keeper(item):
    pattern = r'Hatch_tm(\d*\.\d+|\d+)'
    matched = re.search(pattern, item)
    if matched:
        getcontext().prec = 20
        tm = Decimal(matched[1])
        return tm
    else:
        return None


def csv_logger():
    current = dict.fromkeys(field_names)
    current[field_names[0]] = current_location
    current[field_names[1]] = current_exp
    current[field_names[2]] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('dungeon.csv', "a", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=field_names)
        try:
            writer.writerow(current)
        except BaseException as excep:
            print(f'Жесть какаято с логами:{excep}')


def work_with_location(location):
    # TODO Глобальные переменные соответственно преобразуются в атрибуты класса
    # TODO Что позволит нам помимо прочего облегчить пространство имён, если вдруг мы захотим импортировать
    # TODO куда-то нашу игру.
    global current_exp, remaining_time, current_location
    current_location = list(dict.keys(location))[0]
    values = list(dict.values(location))[0]
    csv_logger()
    print(f'Вы находитесь в локации {current_location}')
    print(f'У вас {current_exp} опыта и осталось {remaining_time} секунд до наводнения')
    if Decimal(remaining_time) < 0:  # TODO Если время равно 0, то тоже должен быть проигрыш
        print("Время вышло. Герой утонул и почил смертью храбрых")
        print("")
        return 1
    print(f'Прошло времени: {get_time_delta(current_date)}')
    print("В локации вы видите: ")
    if len(values) is 0:
        print("Тупичек((((")
        return 1
    for subitem in values:
        if isinstance(subitem, dict):
            for loc in subitem:
                print(f'-- Вход в локацию: {loc}')
        else:
            print(f'-- Монcтра: {subitem}')
    print('Выберите действие:')
    print('1.Атаковать монстра')
    print('2.Перейти в другую локацию')
    print('3.Сдаться и выйти из игры')
    user_input = int(input())
    if user_input is 1:  # TODO С таким сравнением надо быть осторожнее
        # TODO is проверяет идентичность объектов, а не равенство значений
        # TODO Но в некоторый момент два числа могут иметь равное значение, но при этом они могут не быть
        # TODO идентичными объектами (используйте == лучше :) )
        print("Вы выбрали Атаковать монстра")
        
        for subitem in values:
            if not isinstance(subitem, dict):
                exp, tm = atack_monster(subitem)
                current_exp = current_exp + int(exp)
                getcontext().prec = 20
                remaining_time = str(Decimal(remaining_time) - Decimal(tm))
                values.remove(subitem)
                # print(f'Опыта: {current_exp}, Времени до новодненеия: {remaining_time}')
        modifed_dict = {}
        modifed_dict[current_location] = values
        work_with_location(modifed_dict)

    elif user_input is 2:
        print("Вы выбрали Перейти в локацию")

        for subitem in values:
            if isinstance(subitem, dict):
                for loc in subitem:
                    if parse_location(loc):
                        num, tm = parse_location(loc)
                        print(f'{num} .Вход в локацию: {loc}')
                    else:
                        if current_exp >= 280:
                            time_hatch = hatch_keeper(loc)
                            getcontext().prec = 20
                            remaining_time = str(Decimal(remaining_time) - Decimal(time_hatch))
                            # TODO Вот тут ещё стоит проверить, осталось ли время после этого действия
                            # TODO Если время == 0 - то это проигрыш
                            print(f'Осталось времени до наводнеия {remaining_time}')
                            print(list(dict.values(subitem))[0])
                            return 2
                        else:
                            print("Вы добрались до выхода, но нахапали мало экспириенса((Это не позволит открыть дверь")
                            return 1

        user_input_location = input('Введите номер локации:')
        # TODO Любой ввод пользователя стоит снабдить проверками, иначе программа будет неустойчивой
        pattern = r'Location_' + f'{user_input_location}' + r'_tm\d'
        match = None
        for subitem in values:
            if isinstance(subitem, dict):
                for loc in subitem:
                    match = re.findall(pattern, loc)
                    if match:
                        num, tm = parse_location(loc)
                        getcontext().prec = 20
                        remaining_time = str(Decimal(remaining_time) - Decimal(tm))
                        values.remove(subitem)
                        work_with_location(subitem)

        if not match:
            print("Локация с таким номером не доступна")
            modifed_dict = {}
            modifed_dict[current_location] = values
            work_with_location(modifed_dict)
    elif user_input is 3:
        print("Вы выбрали выйти из игры")
        return 2
    else:
        print("Нет такого действия")


def game_canvas():
    global current_exp, remaining_time,current_location,current_date
    with open("rpg.json", "r") as read_file:
        loaded_json_file = json.load(read_file)
    # print(dict.items(loaded_json_file))
    doo = True
    while doo:
        do = work_with_location(loaded_json_file)
        if do is 1:
            doo = False
        else:
            break
    else:
        remaining_time = '123456.0987654321'
        current_exp = 0
        current_location = ''
        current_date = datetime.datetime.now()
        game_canvas()


game_canvas()
# print('Вы находитесь в Location_0_tm0')

# Учитывая время и опыт, не забывайте о точности вычислений!
