#!/usr/bin/env python
# coding:utf-8

from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import *

info = {
    'path':[]
}
def make_app():
    app = Tk()
    app.config(bg='#303030')
    app.geometry('300x300')
    Listbox(app,name='lb1',
            font=('Hack',12,'bold'),
            bg='#303030',
            fg='white').pack(fill=BOTH)
    Button(app,text='find pictures',command=ui_update).pack()
    Button(app,text='compress',command=compress).pack()
    return app

def ui_update():
    files = askopenfilenames()
    info['path'] = files
    lb1 = app.children['lb1']
    if info['path']:
        for name in files:
            lb1.insert(END,name.split('/')[-1])


def compress():
    for file_path in info['path']:
        output = r'C:\Users\xuqing\Desktop\output\\'
        image = Img.open(file_path)
        name = file_path.split('/')[-1]
        image.save(output+name,quality=60)


app = make_app()
app.mainloop()
