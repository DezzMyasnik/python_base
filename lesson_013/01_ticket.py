# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import datetime
import argparse

class TicketMaker:

    def __init__(self, fio, from_place, to, date, save_to=None):
        if (fio, from_place, to, date) is not None:
            self.fio = fio
            self.from_place = from_place
            self.to = to
            self.date = date
        else:
            print("Один из обязательных параметров не указан")

        self.save_to = save_to
        self.template =os.path.join("images", "ticket_template.png")
        self.font_path = os.path.join("python_snippets", "fonts", "ofont_ru_Muller.ttf")


    def make(self):
        im = Image.open(self.template)

        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=16)

        y = im.size[1] - 225 - (10 + font.size) * 2
        draw.text((45, y), self.fio.upper(), font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 155 - (10 + font.size) * 2
        draw.text((45, y), self.from_place.upper(), font=font, fill=ImageColor.colormap['black'])

        y = im.size[1] - 90 - (10 + font.size) * 2
        draw.text((45, y), self.to.upper(), font=font, fill=ImageColor.colormap['black'])


        y = im.size[1] - 90 - (10 + font.size) * 2
        draw.text((280, y), self.date.upper(), font=font, fill=ImageColor.colormap['black'])
        #im.show()
        out_path = self.save_to if self.save_to else 'ticket_out.png'
        im.save(out_path)
        print(f'Post card saved az {out_path}')


if __name__ == '__main__':
    maker = TicketMaker(fio='Оля Иванова', from_place='Ленинград', to='Москва', date='10.10.2019', save_to='ticket_.png')
    maker.make()

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
