#!/usr/bin/env python
# coding:utf-8
'''
删除重复的文件。包括不同文件夹内的重复文件。
需要用到filecmp模块，自己阅读官方文档https://docs.python.org/3/library/filecmp.html，培养自己的自学能力
'''

import filecmp
import os

path = './files'
dirs = ['pic1','pic2']

# 得到两个目录的所有文件列表
def getAllFiles(path,dirs):
    all_files = list()
    for d in dirs:
        curr_path = path + '/' + d
        for f in os.listdir(curr_path):
            all_files.append(curr_path + './' + f)
    return all_files

# 比较两个文件的内容是否一致
def cmp_files(x,y):
    if filecmp.cmp(x,y):
        os.remove(y)
        print("{}是重复文件，已删除".format(y))


all_files = getAllFiles(path,dirs)
for x in all_files:
    for y in all_files:
        if x != y and os.path.exists(x) and os.path.exists(y):
            cmp_files(x,y)
