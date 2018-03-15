#!/bin/env python

#第3天练习：自动压缩文件
#监测 image 文件夹，如果包含的文件大于等于 5 个，则将这些文件压缩到 archive1.zip 文件中，并删除这些文件。当再次监测到文件多于 5 个的时候，生成 archive2.zip 压缩包，以此类推。 
#
#图片素材压缩包：https://video.mugglecode.com/image.zip，请下载后解压使用 
#
#Tips： 
#shutil 库中的 make_archive 函数可以生成压缩包，使用方法如下： 
#make_archive(path1, 'zip', path2) 
#其中 path1 是生成压缩包的路径（包含压缩包名称），path2是需要被压缩的文件夹。
import os,shutil,time

image_path = '/tmp/image'
archive_path = '/tmp/image_archive'
zip_count = 0
while True:
    files = os.listdir(image_path)
    files_count = len(files)
    if files_count >= 5:
        zip_count += 1
        zip_name = archive_path + '/archive' + str(zip_count)
        shutil.make_archive(zip_name,'zip',image_path)
        for f in files:
            os.remove(image_path + '/' + f)
    time.sleep(1)
