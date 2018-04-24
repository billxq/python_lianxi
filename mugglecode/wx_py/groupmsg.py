#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/24 下午3:21
# @author: Bill
# @file: groupmsg.py


from wxpy import *
import csv


def read_info():
    f = open('./files/sample.csv','r')
    reader = csv.DictReader(f)
    return [info for info in reader]

info = read_info()
print(info)