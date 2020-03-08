#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
from settings import *


# https://vk.com/grandminds
log = logging.getLogger('BotLog')
def logconfig():
    """
    Конфигурация логгера
    :return:
    """
    stream_logger = logging.StreamHandler()
    stream_logger.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    stream_logger.setLevel(logging.INFO)
    log.addHandler(stream_logger)


    filehandler = logging.FileHandler(LOG_FILE_NAME, 'a', 'utf-8')
    formatter = logging.Formatter(LOG_FORMAT)
    formatter.datefmt = '%d-%m-%Y %H:%M'
    filehandler.setLevel(logging.DEBUG)
    # все возможные аттрибуты см https://docs.python.org/3.5/library/logging.html#logrecord-attributes
    filehandler.setFormatter(formatter)
    log.addHandler(filehandler)
    log.setLevel(logging.DEBUG)



class Bot:
    def __init__(self, token, group_id):
        """
        Initial vk  bot
        :param token: secret token from vk.com
        :param group_id: group id in vk
        """
        self.vk_token = token
        self.group_id = group_id
        self.vk_session = vk_api.VkApi(token=self.vk_token)
        self.long_poller = VkBotLongPoll(self.vk_session, group_id)
        self.vk = self.vk_session.get_api()

    def run(self):
        """
        запуск прослушивателя longpool сервера
        :return:
        """
        try:
            for event in self.long_poller.listen():
                self.on_event(event)

        except Exception:
            log.exception('Ошибка обработки сообщения')


    def on_event(self, event):
        """
        Обработчик события
        :param event: событие в пришедшее от vk
        :return:
        """

        if event.type is VkBotEventType.MESSAGE_NEW:
            log.debug("пришло сообщение")
            #print(f'Новое сообщение:{event.message.text}')
            self.vk.messages.send(peer_id=event.group_id * (-1),
                                  user_id=event.message.from_id,
                                  chat_id=event.chat_id,
                                  message=event.message.text,
                                  random_id=random.randint(10, 20000000))
        else:
            log.info(f'этого еще не умею. пришло {event.type}')
            #print(f'этого еще не умею. пришло {event.type}')


if __name__ == '__main__':
    logconfig()
    chat_bot = Bot(APIKEY, PUBLIC_ID)
    chat_bot.run()
#зачет!