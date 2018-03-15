#!/bin/env python
# 作用：将不同后缀名的文件整理到以对应后缀名命名的文件夹中，使用前先修改path的值
import os
import shutil

# path = r'C:\Users\Administrator\Documents\My RTX Files\xuqing10'
path = r'C:\Users\Administrator\Documents\My RTX Files\xuqing10'
os.chdir(path)
files = os.listdir(path)
for f in files:
    folder_name = os.path.join(path,f.split('.')[-1])
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(f,folder_name)
    else:
        shutil.move(f,folder_name)
