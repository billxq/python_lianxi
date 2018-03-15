#!/usr/env python
# coding:utf-8

#第1天练习：如何模糊搜索文件
#下载并解压这个文件素材压缩包 https://video.mugglecode.com/files.zip，然后使用 Python 从这中筛选出符合这些特征的文件： 
#1. 除了 gif 类型之外的其他类型 
#2. 名字中包含有关键词 “project30”或者“commercial”

import os
import shutil

path = './'
files = os.listdir(path)

for f in files:
    if not f.endswith('.gif') and ('project30' in f or 'commerical' in f):
        print(f)
