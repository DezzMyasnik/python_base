#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import random

import handlers
import settings
import vk_api
from settings import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

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


class UserSate:
    """Состояне пользователя пр нахождении внутри сценария"""

    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


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
        self.user_states = dict()

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

        if event.type is not VkBotEventType.MESSAGE_NEW:
            log.info(f'этого еще не умею. пришло {event.type}')
            return
        log.debug("пришло сообщение")
        # print(f'Новое сообщение:{event.message.text}')
        user_id = event.message.from_id
        text = event.message.text
        if user_id in self.user_states:
            text_to_send = self.continue_scenario(user_id, text=text)
        else:
            # search intetnt
            for intent in settings.INTENTS:
                if any(token in text.lower() for token in intent['tokens']):
                    # run intetnt
                    log.debug(f'User {user_id} получил {intent}')
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER
        self.vk.messages.send(peer_id=event.group_id * (-1),
                              user_id=user_id,
                              chat_id=event.chat_id,
                              message=text_to_send,
                              random_id=random.randint(10, 20000000))

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserSate(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            # next step
            next_step = steps[step["next_step"]]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                # switch to next step
                state.step_name = step['next_step']
            else:
                # finish
                log.info("Зарегистрирован {name} с почтой {email}".format(**state.context))
                self.user_states.pop(user_id)
        else:
            text_to_send = step['failure_text'].format(**state.context)
        return text_to_send


if __name__ == '__main__':
    logconfig()
    chat_bot = Bot(APIKEY, PUBLIC_ID)
    chat_bot.run()
