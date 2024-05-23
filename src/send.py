#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : send.py
# @Author   : jade
# @Date     : 2024/5/23 9:30
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
import requests as rq

class Send:
    def __init__(self, token):
        self.token = token

    def tg_send(self, chat_id, text):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text
        }
        rq.post(url, data=data)