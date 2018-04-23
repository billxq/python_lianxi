#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/23 下午1:25
# @author: Bill
# @file: compress_pics.py

from tkinter import *
from tkinter.filedialog import *
from PIL import Image as Img

info = {
    'path':[]
}

def make_app():
    app = Tk()
    Label(app,text='图片压缩小工具',font=('Arial',25,'bold')).pack()
    Listbox(app,name='lbox',bg='#f2f2f2',fg='red').pack(fill=BOTH,expand=True)
    Button(app,text='open',command=ui_getdata).pack()
    Button(app,text='compress',command=compress).pack()
    app.geometry('300x400')
    return app

def ui_getdata():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    if info['path']:
        for f in f_names:
            lbox.insert(END,f.split('/')[-1])

def compress():
    for f_name in info['path']:
        output = '/Users/xuqing/Desktop/output/'
        name = f_name.split('/')[-1]
        image = Img.open(f_name)
        image.save(output+'c_'+name,quality=60)

app = make_app()
app.mainloop()
