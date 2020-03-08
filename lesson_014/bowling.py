# -*- coding: utf-8 -*-


class ScoreCounter:


    def get_score(self,game_result):

        valid_data = {
            'X': 20,
            '/': 15,
            '-': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,

        }

        score = 0
        counter = 0
        subcounter = 0
        for i,item in enumerate(game_result):

            if item in valid_data:
                score += valid_data[item]
                if subcounter == 2:
                    counter += 1
                    subcounter = 0
                if item is 'X':
                    subcounter += 2
                elif item is '/':
                    if subcounter is 0:
                         raise ValueError("Не верная запись результата")

                    score -= int(game_result[i-1])
                    subcounter += 1
                elif item is '-':
                    subcounter += 1
                else:
                    if subcounter is 1 and valid_data[item]+valid_data[game_result[i-1]] >=10:
                       raise ValueError("Не верная запись результата")
                    subcounter += 1
            else:
                raise ValueError("Не верная запись результата")
            if counter > 9:
                raise ValueError('Длина строки с результатами превышает допустимую длину')

        if counter is 9 and subcounter is 2:

            return score
        else:
            raise ValueError("Короткая строка с результатом")


# зачет!
