# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

import os
from collections import defaultdict
import multiprocessing
import time
from python_snippets.utils import time_track



class ProcessTiker(multiprocessing.Process):

    def __init__(self, file_name, ticker_volatilnost, collector, *args, **kwargs):
        super(ProcessTiker, self).__init__(*args, **kwargs)
        self.full_file_name = file_name
        self.ticker_volat = ticker_volatilnost
        self.collector = collector

    def run(self):
        maximum = 0
        minimum = 0
        first = True
        with open(self.full_file_name, 'r', encoding='utf-8') as f_file:
            f_file.readline()
            for line in f_file:
                if not first:
                    try:
                        varible = float(line[:-1].split(',')[2])
                        if varible > maximum:
                            maximum = varible

                        if varible < minimum:
                            minimum = varible
                    except BaseException as exc:
                        print(exc)
                else:
                    first_init = line[:-1].split(',')
                    maximum = minimum = float(first_init[2])
                    ticker_name = first_init[0]
                    first = False

            try:
                average_price = (maximum + minimum) / 2

                volatility = ((maximum - minimum) / average_price) * 100
                self.ticker_volat[ticker_name] += volatility
                self.collector.put([ticker_name, volatility])
                # with self.ticker_volat_lock:
                #    self.ticker_volat[ticker_name] += volatility

            except (ValueError, BaseException) as exc:
                print(exc)


@time_track
def main():
    dir = 'trades'

    full_dir_name = os.path.join(os.getcwd(), dir)

    tickers = defaultdict(float)
    # lock = threading.Lock()
    collector = multiprocessing.Queue()
    ticker_process = [ProcessTiker(file_name=os.path.join(full_dir_name, file), ticker_volatilnost=tickers,
                                   collector=collector) for file in os.listdir(full_dir_name)]

    for threads in ticker_process:
        threads.start()

    for threads in ticker_process:
        threads.join()

    ended_tickers = []
    while not collector.empty():
        data = collector.get()
        ended_tickers.append(data)


    ended_tickers.sort(key=lambda i: -i[1])
    result = [x for x in ended_tickers if x[1] > 0]
    print('Маскимальная волатильнсть')
    [print(f'{tick} - {round(volat, 2)}%') for (tick, volat) in result[:3]]

    print('Минимальная волатильнсть')

    [print(f'{tick} - {round(volat, 2)}%') for (tick, volat) in result[-3:]]

    print('Нулевая волатильнсть')

    ended_tickers.sort(key=lambda x: x[0])
    print(','.join(x[0] for x in ended_tickers if x[1] == 0))


if __name__ == '__main__':
    main()
