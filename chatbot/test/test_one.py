#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import Mock, patch, ANY
from vk_api.bot_longpoll import VkBotMessageEvent
from bot import Bot
class TestBot(unittest.TestCase):

    RAW_DATA = {'type': 'message_new',
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
            event = [obj]*count
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

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_DATA)
        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('','')
                bot.vk = Mock()
                bot.vk.messages.send = send_mock
                bot.on_event(event)

        send_mock.assert_called_once_with(
            peer_id=self.RAW_DATA['group_id']*-1,
            user_id=self.RAW_DATA['object']['message']['from_id'],
            chat_id=ANY,
            message=self.RAW_DATA['object']['message']['text'],
            random_id=ANY
        )

if __name__ == '__main__':
    unittest.main()