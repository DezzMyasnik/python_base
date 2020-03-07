# -*- coding: utf-8 -*-


class ScoreCounter:


    def get_score(self,game_result):

        valid_data = ['X','/','-']
        valid_data.extend(range(1,10))
        #if game_result[0] is '/':
        #    raise ValueError("Не верная запись результата")
        game_result = list(game_result)
        score = 0
        counter = 0
        subcounter = 0
        for i,item in enumerate(game_result):

            if item.isdigit():
                item = int(item)
            if item in valid_data:
                if subcounter == 2:
                    counter += 1
                    subcounter = 0
                if item is 'X':
                    score += 20
                    subcounter += 2
                elif item is '/':
                    if subcounter is 0:
                         raise ValueError("Не верная запись результата")

                    score -= int(game_result[i-1])
                    score += 15
                    subcounter += 1
                elif item is '-':
                    subcounter += 1
                else:
                    score += item
                    subcounter += 1
            else:
                raise ValueError("Не верная запись результата")
            if counter > 9:
                raise ValueError('Длина строки с результатами превышает допустимую длину')

        if counter is 9 and subcounter is 2:

            #print(counter)
            return score
        else:
            raise ValueError("Короткая строка с результатом")


#  2) принимает неправильные
#TODO  'X'*9 + '55' а почему это не правильный результат?

