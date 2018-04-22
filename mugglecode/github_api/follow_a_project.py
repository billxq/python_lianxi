#!/usr/bin/env python
# coding:utf-8

'''
检测github上的一个项目，如果项目更新就自动打开网页，用到了github提供的api接口
实时监测需要用到死循环:
while 1:
    do something
我关注的项目是大师兄直播课的一个repo，api接口:
https://api.github.com/repos/ajing2/LivePython1
思维代码：
if last_update < cur_update:
    open(webbrowser)
'''
import webbrowser
import requests
import time

project_url = 'https://github.com/ajing2/LivePython1'
api = 'https://api.github.com/repos/ajing2/LivePython1'

last_update = None

while 1:
    all_info = requests.get(api).json()  # 返回的是json数据，要把它转换为python的dict数据，requests库有json方法可以做到，这样一来all_info就是一个字典
    cur_update = all_info['updated_at']  # 获取一个最后更新的时间，用来和上一次获取的时间做对比，返回的时间格式是：2018-04-19T14:49:06Z，只要格式一样，两个时间可以对比大小
    if not last_update:
        last_update = cur_update

    if last_update < cur_update:
        webbrowser.open(project_url)  # webbrowser模块默认打开默认浏览器
    time.sleep(600)