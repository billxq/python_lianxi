#!/bin/env python
#第3天练习：如何删除重复文件
#下载并解压这个文件素材压缩包 https://video.mugglecode.com/problem3_files.zip ，然后使用 Python 进行这样的操作： 
#删除重复的文件。包括不同文件夹内的重复文件。 
#
#文档阅读力培养： 
#阅读 filecmp 文档中关于 filecmp.cmp 的那一段说明，文档地址：https://docs.python.org/3/library/filecmp.html
import os,shutil
import filecmp
path = '/tmp/problem3_files'
dirs = ['pic1','pic2']
def get_all_files(path,dirs):
    all_files = []
    for d in dirs:
        cur_path = path + '/' + d
        for f in os.listdir(cur_path):
            all_files.append(cur_path + '/' + f)
    return all_files

#print(get_all_files(path,dirs)) 

def cmp_files(x,y):
    if filecmp.cmp(x,y):
        os.remove(y)
        print("路径\"" + y + "\"下的文件是重复文件已删除")

all_files = get_all_files(path,dirs)
for x in all_files:
    for y in all_files:
        if x != y and os.path.exists(x) and os.path.exists(y):
            cmp_files(x,y)
