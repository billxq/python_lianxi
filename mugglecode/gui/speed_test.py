#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/24 下午2:05
# @author: Bill
# @file: speed_test.py

"""
用来实时监测网络速度
"""
from tkinter import *
import psutil
import time

def make_app():
    app = Tk()
    app.config(bg='black')
    Label(app,text='Net Speed Test',font=('Hack',20,'bold'),bg='black',fg='red').pack()
    Label(app,name='lb',text='_kb/s',font=('Hack',20),bg='black',fg='white').pack(fill=BOTH,expand=True)
    app.geometry('200x150')
    return app


def get_speed():
    s1 = psutil.net_io_counters(pernic=True)['en0']
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=True)['en0']
    delta = s2.bytes_recv - s1.bytes_recv
    speed = delta / 1024
    return str(speed) + 'kb/s'

def ui_update(func):
    data = func()
    lb = app.children['lb']
    lb.config(text=data)
    app.after(1000,lambda :ui_update(func))

app = make_app()
app.after(1000,lambda :ui_update(get_speed))
app.mainloop()