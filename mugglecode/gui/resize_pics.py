#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/24 上午10:00
# @author: Bill
# @file: resize_pics.py

'''
提示文案：请上传正方形图片，点击「打开」按钮可以输入多张图片，
点击「生成」可以等比例生成指定多个尺寸（50×50、100×100、120×120、180×180、512×512）的大小。界面与思路和课程中类似。
'''
from tkinter import *
from tkinter.filedialog import *
from PIL import Image as Img

size = [50,100,120,180,512]

info = {
    'path':[]
}

def make_app():
    app = Tk()
    Label(app,text='resize pictures',font=('hack',20,'bold')).pack()
    Listbox(app,name='lbox',bg='#f2f2f2',fg='black').pack(fill=BOTH,expand=True)
    Button(app,text='open',command=get_uidata).pack()
    Button(app,text='100x100',command=resize_pic).pack()
    app.geometry('300x400')
    return app


def get_uidata():
    f_name = askopenfilenames()
    info['path'] = f_name
    if info['path']:
        for f in f_name:
            lbox = app.children['lbox']
            lbox.insert(END,f.split('/')[-1])

def resize_pic():
    for f in info['path']:
        output = '/Users/xuqing/Desktop/output'
        name = f.split('/')[-1]
        image = Img.open(f)
        for s in size:
            image.resize((s,s)).save(f'{output}/{s}_{name}')


app = make_app()
app.mainloop()

