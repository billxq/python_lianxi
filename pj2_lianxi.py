#!/usr/env python
# coding:utf-8

#下载并解压这个文件素材压缩包 https://video.mugglecode.com/problem2_files.zip，然后使用 Python 进行这样的操作： 
#1. 把 jpg,png,gif 文件夹中的所有文件移动到 image 文件夹中，然后删除 jpg,png,gif 文件夹 
#2. 把 doc,docx,md,ppt 文件夹中的所有文件移动到 document 文件夹中，然后删除

#问题拆解提示：
#如何实现文件归类可以拆解为以下4个子问题：
#1.如何创建目标文件夹？
#2.如何浏览各个文件夹？
#3.如何移动文件夹中的文件？
#4.如何删除文件夹？
#问题解决提示：
#1. 利用 os 模块中的 makedirs 函数，可以在指定路径创建文件夹。在本题中，可以先创建好 image 和 document 文件夹，在进行后续的处理。
#2. os 模块中的 listdir 函数和 for 语句配合，可以完成浏览文件夹中所有文件的功能。在本题中需要注意的是，要浏览的文件夹有7个，所以先将这7个文件夹的名称存到了 list 变量中，便于使用。
#3. shutil 模块中的 move 函数提供了移动文件的功能。需要指定文件所在路径和目标路径。
#4. os 模块中的 removedirs 函数提供了删除文件夹的功能。
import os,shutil
path = './'
#files = os.listdir(path)

if not os.path.exists('images') or not os.path.exists('document'):
    os.makedirs('images')
    os.makedirs('document')


images = ['png','jpg','gif']
document = ['doc','docx','ppt','md']

for d in images:
    images_path = './' + d
    files = os.listdir(images_path)
    for f in files:
        shutil.move(images_path+'/'+f,'./images')
    os.removedirs(images_path)


for d in document:
    docs_path = './' + d
    files = os.listdir(docs_path)
    for f in files:
        shutil.move(docs_path+'/'+f,'./document')
    os.removedirs(docs_path)
