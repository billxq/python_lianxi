#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/23 上午9:11
# @author: Bill
# @file: repo_starredbyKenneth.py
"""
Kenneth Reitz 是 Python 领域的大神级人物，并且在 Github 上非常活跃，他的 Github 地址是：https://github.com/kennethreitz
试着用所学知识去发现 Kenneth 今天 Starred 了哪些库，并且自动在浏览器中打开这些库的地址。
"""
import time
import webbrowser

import requests
api = 'https://api.github.com/users/kennethreitz/starred'

# 创建一个空列表用来存放Kenneth starred的用户id
starred = list()
all_info = requests.get(api).json()
for info in all_info:
    starred.append(info['id'])


# 定义一个死循环，每10分钟检测一下有没有新的id，有就打开新starred的用户的repo
while 1:
    results = requests.get(api).json()
    for result in results:
        if result['id'] not in starred:
            starred.append(result['id'])
            url = result['html_url']
            webbrowser.open()
        print(result['html_url'])
    time.sleep(600)



