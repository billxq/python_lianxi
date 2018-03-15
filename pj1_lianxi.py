#!/usr/env python
# coding:utf-8

#第1天练习：如何模糊搜索文件
#下载并解压这个文件素材压缩包 https://video.mugglecode.com/files.zip，然后使用 Python 从这中筛选出符合这些特征的文件： 
#1. 除了 gif 类型之外的其他类型 
#2. 名字中包含有关键词 “project30”或者“commercial”

#问题拆解提示：
#如何模糊搜索文件可以拆解为以下3个子问题：
#1.怎样指定路径？
#2.怎样浏览路径下的所有文件？
#3.怎样检查文件名是否符合要求？
#问题解决提示：
#1.设定 path 变量，存储题目给定的相对路径。相对路径以符号“.”开头，用符号“/”分割文件夹。
#2.利用 os 模块中的 listdir 函数，将路径中的所有文件存储到一个 list 变量中。然后，利用 for 语句浏览 list 变量中的所有元素。
#3.利用 if 语句判断文件名是否符合要求。其中，endswith 函数用来判断一个字符串是否包含某个后缀。成员运算符 in 用来判断一个字符串是否包含某个子串。不同的条件用 and或者 or 来连接。

import os
import shutil

path = './'
files = os.listdir(path)

for f in files:
    if not f.endswith('.gif') and ('project30' in f or 'commerical' in f):
        print(f)
