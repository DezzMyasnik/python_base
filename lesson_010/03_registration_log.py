# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


from collections import defaultdict


class NotNameError(BaseException):
    pass


class NotEmailError(BaseException):
    pass


class Parser:

    def __init__(self, filename):
        self.name = filename
        self.log = []
        self.stata = defaultdict(int)

    def read_log(self):
        with open(self.name, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    self.line_process(line[:-1])
                    self.write_log(line)
                except (ValueError, NotNameError, NotEmailError) as exc:
                    print(f"Ошибка типа: {exc}")
                    self.write_erorr_log(f"{exc} \n")

    def line_process(self, line):
        rout = line.split(' ')

        if len(rout) != 3:
            raise ValueError('В строке менше трех элементов', line)
        if not rout[0].isalpha():
            raise NotNameError('В имени не только буквы', line)
        if '@' not in rout[1] or '.' not in rout[1]:
            raise NotEmailError('Не соотвесвтует формату почты', line)
        if rout[2].isdigit():

            if 10 > int(rout[2]) or int(rout[2]) > 99:
                raise ValueError("Не в диапазоне от 10 до 99", line)

        else:
            raise ValueError('Поле возраста не число', line)

    def write_log(self, line):
        with open('registrations_good.log', 'a', encoding='utf-8') as file:
            file.writelines(line)

    def write_erorr_log(self, line):
        with open(' registrations_bad.log', 'a', encoding='utf-8') as file:
            file.writelines(line)


log = Parser('registrations.txt')
log.read_log()
#зачет!