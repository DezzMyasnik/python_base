#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('я')
my_family.append('отец')
my_family.append('мама')
#print(my_family)
# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]
my_family_height[0] = [my_family[0], 187]
my_family_height.append([my_family[1], 183])
my_family_height.append([my_family[2], 167])

#print(my_family_height)
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

for r in my_family_height:
    if r[0] == 'отец':
        print("Рост отца - {} cм".format(r[1]))

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

rost = 0

for r in my_family_height:
    rost += r[1]

print("Общий рост семьи - {} cм".format(rost))