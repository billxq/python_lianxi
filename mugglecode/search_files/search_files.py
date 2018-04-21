#!/usr/bin/env python
# coding:utf-8

"""
在files文件夹中搜索
1. 除了 gif 类型之外的其他类型 
2. 名字中包含有关键词 “project30”或者“commercial”
"""
import os

path = "./files"
for f in os.listdir(path):
    if ("project30" in f or "commercial" in f) and (not f.endswith('.gif')):
        print(f)