#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/27 上午9:48
# @author: Bill
# @file: module_demon.py
#
# from io import StringIO  # 引入StringIO
# f = StringIO()          # 实例化
# f.write('Hello\n')  # 通过write函数将字符串写入内存
# print('Bill',file=f)
# print(f.getvalue())  # 通过getvalue方法得到内存缓冲区的所有内容
# f.close()
#
# print('-'*10)
#
# f = StringIO('Hello world\nPython is good!')  # 可以在实例化时直接将字符串写入内存
# while 1:                # 通过循环语句以及readline函数读取缓冲区内容
#     s = f.readline()
#     if s == '':   # 如果达到结尾
#         break
#     print(s.strip())
#
# print('-'*10)


from io import BytesIO
f = BytesIO()  # 实例化一个bytesio
f.write('我爱学习！'.encode('utf-8'))   # 写入的内容要经过utf-8编码
print(f.getvalue())

print('-'*10)

f = BytesIO(b'\xe6\x88\x91\xe7\x88\xb1\xe5\xad\xa6\xe4\xb9\xa0\xef\xbc\x81')   # 可以用一个bytes初始化BytesIO，然后，像读文件一样读取
print(f.read())
