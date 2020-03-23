#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import unittest
from unittest.mock import Mock, patch

import settings
from bot import Bot
from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEventType


class TestBot(unittest.TestCase):
    RAW_DATA = {'type': VkBotEventType.MESSAGE_NEW,
                'object':
                    {'message':
                         {'date': 1579013554,
                          'from_id': 22002286,
                          'id': 368,
                          'out': 0,
                          'peer_id': 22002286,
                          'text': 'gdfgdfgdfgdfgdf',
                          'conversation_message_id': 73,
                          'fwd_messages': [],
                          'important': False,
                          'random_id': 0,
                          'attachments': [],
                          'is_hidden': False},
                     'client_info':
                         {'button_actions':
                              ['text', 'vkpay', 'open_app', 'location', 'open_link'],
                          'keyboard': True,
                          'inline_keyboard': True,
                          'lang_id': 0}},
                'group_id': 130111251,
                'event_id': '22d14fb9553e9707375723b522669d28dcc42b7a'}

    def test_run(self):
        with patch('bot.vk_api.VkApi'):
            count = 5
            obj = {}
            event = [obj] * count
            long_poller_mok = Mock(return_value=event)
            long_poller_listen_mok = Mock()
            long_poller_listen_mok.listen = long_poller_mok
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mok):
                bot = Bot('', '')
                bot.on_event = Mock()

                bot.run()
                bot.on_event.accert_called()
                bot.on_event.accert_any_call(obj)
                assert bot.on_event.call_count == count

    INPUTS = [
        'Привет',
        'А когда?',
        'Где будет конференция?',
        'Зарегистрируйте меня',
        'Веня',
        'мой адрес mail@mail',
        'mail@mail.ru'
    ]

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.INTENTS[1]['answer'],
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step3']['text'].format(name='Веня', email='mail@mail.ru')

    ]

    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []

        for input_text in self.INPUTS:
            event = copy.deepcopy(self.RAW_DATA)
            # event['chat_id'] = ANY
            # event['random_id'] = ANY
            event['object']['message']['text'] = input_text
            events.append(VkBotMessageEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('bot.vk_api.VkApi') and patch('bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot('', '')
            bot.vk = api_mock
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)
        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])

        assert real_outputs == self.EXPECTED_OUTPUTS




if __name__ == '__main__':
    unittest.main()

