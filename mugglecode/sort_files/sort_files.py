#!/usr/bin/env python
# coding:utf-8

"""
在files文件夹中（files_bak为备份文件夹，以防操作错误）
1. 把 jpg,png,gif 文件夹中的所有文件移动到 image 文件夹中，然后删除 jpg,png,gif 文件夹 
2. 把 doc,docx,md,ppt 文件夹中的所有文件移动到 document 文件夹中，然后删除
"""

import os
import shutil

path = "./files"
files = os.listdir(path)
pic_path = path + '/image'
doc_path = path + '/document'
if not os.path.exists(pic_path) or not os.path.exists(doc_path):
    os.makedirs(pic_path)
    os.makedirs(doc_path)

for f in files:
    if f == "doc":
        for i in os.listdir(path+'/doc'):
            shutil.move(path+'/doc/'+i,doc_path)
        os.removedirs(path+'/doc')
    if f == "docx":
        for i in os.listdir(path+'/docx'):
            shutil.move(path+'/docx/'+i,doc_path)
        os.removedirs(path+'/docx')
    if f == "ppt":
        for i in os.listdir(path+'/ppt'):
            shutil.move(path+'/ppt/'+i,doc_path)
        os.removedirs(path+'/ppt')
    if f == "md":
        for i in os.listdir(path+'/md'):
            shutil.move(path+'/md/'+i,doc_path)
        os.removedirs(path+'/md')
    if f == "gif":
        for i in os.listdir(path+'/gif'):
            shutil.move(path+'/gif/'+i,pic_path)
        os.removedirs(path+'/gif')
    if f == "png":
        for i in os.listdir(path+'/png'):
            shutil.move(path+'/png/'+i,pic_path)
        os.removedirs(path+'/png')
    if f == "jpg":
        for i in os.listdir(path+'/jpg'):
            shutil.move(path+'/jpg/'+i,pic_path)
        os.removedirs(path+'/jpg')

"""
参考代码：
# coding:utf-8
import os
import shutil
# 需要把路径替换成你的文件夹所在路径，当把这个代码文件放在要处理的文件夹外一层时，可以使用下面的相对路径写法
path = './problem2_files'
# 创建目标文件夹
os.makedirs(path + '/image')
os.makedirs(path + '/document')
# 将需要处理的后缀名存储到list中
image_suffix = ['jpg', 'png', 'gif']
doc_suffix = ['doc', 'docx', 'ppt', 'md']
# 移动jpg、png、gif文件中的文件
for i in image_suffix:
    cur_path = path + '/' + i
    files = os.listdir(cur_path)
    for f in files:
        # 移动文件夹中的文件
        shutil.move(cur_path + '/' + f, path + '/image')
    # 删除文件夹
    os.removedirs(cur_path)
# 移动doc、docx、md、ppt文件夹中的文件，步骤与前面类似
for d in doc_suffix:
    cur_path = path + '/' + d
    files = os.listdir(cur_path)
    for f in files:
        shutil.move(cur_path + '/' + f, path + '/document')
    os.removedirs(cur_path)
"""