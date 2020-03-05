# -*- coding: utf-8 -*-


class ScoreCounter:


    def get_score(self,game_result):

        valid_data = ['X','/']  # TODO а '-'?
        valid_data.extend(range(1,10))  # TODO для быстрого поиска правильнее использовать другой контейнер 
        if game_result[0] is '/':
            raise ValueError("Не верная запись результата")
        game_result = list(game_result)
        score = 0
        counter = 0
        subcounter =0
        for i in range(len(game_result)):  # TODO удобнее использовать enumerate

            if game_result[i].isdigit():
                game_result[i] = int(game_result[i])
            if game_result[i] in valid_data:
                if subcounter == 2:
                    counter += 1
                    subcounter = 0
                if game_result[i] is 'X':
                    score += 20
                    subcounter += 2
                elif game_result[i] is '/':
                    score -= game_result[i-1]
                    score += 15
                    subcounter += 1
                else:
                    score += game_result[i]
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

# TODO ваше решение
#  1) отклоняет правильные строки
#  'X'*9 + '--'

#  2) принимает неправильные
#  'X'*9 + '55'
#  'X'*9 + '/2' - unsupported operand type(s) for -=: 'int' and 'str' странная ошибка

