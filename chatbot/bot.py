#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

APIKEY = '3373bf96b11f8169de9c85c56224e2134b185c192bd3dc637de8bdd06bbee6afff681620ea2382bf1a8d8'
PUBLIC_ID = 130111251


# TODO https://vk.com/grandminds

class Bot:

    def __init__(self, token, group_id):
        self.vk_token = token
        self.group_id = group_id
        self.vk_session = vk_api.VkApi(token=self.vk_token)
        self.long_poller = VkBotLongPoll(self.vk_session, group_id)
        self.vk = self.vk_session.get_api()

    def run(self):
        try:
            for event in self.long_poller.listen():
                self.on_event(event)

        except Exception as exc:
            print(f'Ошибка:{exc}')

    def on_event(self, event):

        if event.type is VkBotEventType.MESSAGE_NEW:
            print(f'Новое сообщение:{event.message.text}')
            self.vk.messages.send(peer_id=event.group_id * (-1),
                                  user_id=event.message.from_id,
                                  chat_id=event.chat_id,
                                  message=f'я Вас услышал, Вы сказали: {event.message.text}'.upper(),
                                  random_id=random.randint(10, 20000000))
        else:
            print(f'этого еще не умею. пришло {event.type}')


if __name__ == '__main__':
    chat_bot = Bot(APIKEY, PUBLIC_ID)
    chat_bot.run()
