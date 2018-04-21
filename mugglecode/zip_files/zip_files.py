#!/usr/bin/env python
# coding:utf-8

"""
监测 image 文件夹，如果包含的文件大于等于 5 个，则将这些文件压缩到 archive1.zip 文件中，并删除这些文件。
当再次监测到文件多于 5 个的时候，生成 archive2.zip 压缩包，以此类推。 
Tips： 
shutil 库中的 make_archive 函数可以生成压缩包，使用方法如下： 
make_archive(path1, 'zip', path2) 
其中 path1 是生成压缩包的路径（包含压缩包名称），path2是需要被压缩的文件夹。
"""
import os
import shutil
import time

pic_path = './image'  # 图片目录
zip_path = './'  # 图片压缩包的存放目录，即当前目录

# 定义一个死循环，来实时监控image文件夹的文件数量
zip_count = 1  # 压缩的次数，用来给压缩包命名
while 1:
    pic_files = os.listdir(pic_path)  # 定义一个文件列表，os.listdir()返回一个文件列表
    files_count = len(pic_files)
    if files_count >= 5:
        archive_name = zip_path + 'archive' + str(zip_count)
        shutil.make_archive(archive_name,'zip',pic_path)
        for f in pic_files:
            os.remove(pic_path + '/' + f)
        zip_count += 1
    time.sleep(5)

