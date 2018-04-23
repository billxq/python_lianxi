#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/23 下午1:05
# @author: Bill
# @file: show_pyhtonpkgs.py

'''
用gui显示python安装的第三方库
1.利用pip库中的get_installed_distributions函数，获取第三方库的列表。
2.利用tkinter库中的listbox组件，将列表显示在窗口中。
'''
from tkinter import *
import os
import pip

app = Tk()
label = Label(text='Show all packages',font=('Arial',25,'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2',fg='red')
listbox.pack(fill=BOTH,expand=True)
pkgs = pip.get_installed_distributions()
for pkg in pkgs:
    listbox.insert(END,pkg.key)
app.mainloop()1.利用pip库中的get_installed_distributions函数，获取第三方库的列表。
2.利用tkinter库中的listbox组件，将列表显示在窗口中。