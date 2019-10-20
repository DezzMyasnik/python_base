# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
class Sorter:

    def __init__(self,inputDir,outDir):
        inputDir_normalized = os.path.normpath(inputDir)
        outDir_normalized = os.path.normpath(outDir)
        self.inputDir = inputDir_normalized
        self.outDir = outDir_normalized

    def get_files(self):
        for dirpath, dirnames, filenames in os.walk(self.inputDir):

            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                file_time = self.get_file_attrebutes(full_file_path)
                self.make_dir(file_time)
                self.copy_files(full_file_path)
                #print(full_file_path, secs, file_time)
                #if file_time[0] == 2013:
                    # выводим только файлы за 2013 год

    def make_dir(self, file_time):
        if os.path.exists(os.path.join(self.outDir, str(file_time.tm_year))):
            if not os.path.exists(os.path.join(self.outDir,str(file_time.tm_year), str(file_time.tm_mon))):
                os.makedirs(os.path.join(self.outDir,str(file_time.tm_year), str(file_time.tm_mon)))

        else:
            os.makedirs(os.path.join(self.outDir, str(file_time.tm_year)))
            self.make_dir(file_time)


    def get_file_attrebutes(self,full_file_path):
        secs = os.path.getmtime(full_file_path)
        return time.gmtime(secs)

    def copy_files(self, filename):
        dirname, fname= os.path.split(filename)
        file_time = self.get_file_attrebutes(filename)
        outputName = os.path.join(self.outDir,str(file_time.tm_year), str(file_time.tm_mon), fname)
        shutil.copy2(filename,outputName)



inputDir = os.path.join(os.path.dirname(__file__),'icons')
outDir  = os.path.join(os.path.dirname(__file__),'icons_by_year')
test = Sorter(inputDir, outDir )

test.get_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
