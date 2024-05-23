#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : main.py
# @Author   : jade
# @Date     : 2024/5/23 9:25
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from src.quarkCheckin import Quark
from src.aliCheckin import Aliyundrive
from src import send
import argparse
import re

def quarkCheckIn(args):
    quarkCookieList = args.quarkCookie.split(",")
    msg = ""
    print("✅检测到共{}个夸克账号".format(len(quarkCookieList)) )
    for idx, token in enumerate(quarkCookieList):        # 开始任务
        log = f"🙍🏻‍♂️ 第{idx + 1}个夸克云盘账号"
        msg += log
        # 登录
        log = Quark(token).do_sign()
        print("🙍🏻‍♂️ 第{}个账号{}".format(idx+1,log))
        msg += log + "\n"
    return msg

def aliCheckin(args):
    aliTokenList = args.aliToken.split(',')
    ali = Aliyundrive()
    message_all = ""
    print("✅检测到共", len(aliTokenList), "个阿里云盘账号")
    for idx, token in enumerate(aliTokenList):
        result = ali.aliyundrive_check_in(token,idx)
        print(str(result)+"\n")
        message_all = message_all + str(result) + "\n"
    return message_all



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--aliToken", help="ali Token",default="", type=str)
    parser.add_argument("--quarkCookie", help="quark Cookie",default= "",type=str)
    parser.add_argument("--telChatId", help="",default= "",type=str)
    parser.add_argument("--telToken", help="",default= "",type=str)

    args = parser.parse_args()
    msg = ""
    msg = msg + quarkCheckIn(args)
    msg = msg + aliCheckin(args)

    sender = send.Send(args.telToken)
    sender.tg_send(args.telChatId, msg)

