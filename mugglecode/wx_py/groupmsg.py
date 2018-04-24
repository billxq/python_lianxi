#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/24 下午3:21
# @author: Bill
# @file: groupmsg.py


'''
利用微信的wxpy模块，批量发送消息
'''
import time

from wxpy import *
import csv



def read_info():
    f = open('./files/sample.csv','r')
    reader = csv.DictReader(f)
    return [info for info in reader]

def make_message(raw_info):
    temp = '{n}-同学请于{t}时间参加{s}课程，课程地址是{a}。收到请回复，谢谢!'
    msg_list = [temp.format(n=info['姓名'],
                            t=info['上课时间'],
                            s=info['课程'],
                            a=info['上课地址']) for info in raw_info]
    return msg_list


def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        friend_name = msg.split('-')[0]
        f = bot.friends().search(friend_name)
        if len(f) == 1:
            f[0].send(msg)
        else:
            print(friend_name)
            print('Please check this name!')
        time.sleep(3)


raw_info = read_info()
msg_list = make_message(raw_info)
send(msg_list)