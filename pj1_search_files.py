#!/bin/env python
import os

path = './'
files = os.listdir(path)
a = input('请输入查找文件的关键字：')


for f in files:
    if a in f:
        print(f)
