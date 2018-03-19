#!/usr/bin/env python
# coding:utf-8
import psutil
from tkinter import *

import time


def make_app():
    app = Tk()
    app.config(bg='#303030')
    Label(name='lb1',
          text='实时网速',
          font=('Hack',25,'bold'),
          bg='#303030',
          fg='red').pack()
    Label(name='lb2',
          text='_KB/S',
          font=('Hack',25,'bold'),
          bg='#303030',
          fg='red').pack()
    app.geometry('300x150')
    return app


def get_speed():
    s1 = psutil.net_io_counters(pernic=True)['WLAN'].bytes_recv
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=True)['WLAN'].bytes_recv
    result = (s2 - s1)/1024
    return '%.2f'%result + 'KB/S'

def ui_upate(do):
    data = do()
    lb2 = app.children['lb2']
    lb2.config(text=data)
    app.after(1000,lambda : ui_upate(do))





app = make_app()
app.after(1000,lambda : ui_upate(get_speed))
app.mainloop()

