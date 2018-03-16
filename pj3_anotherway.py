#!/bin/env python
# coding:utf-8

import os,filecmp

x = filecmp.dircmp('./pic1','./pic2')
same_files = x.same_files
print(same_files)

for f in same_files:
    if f in os.listdir('./pic1'):
        os.remove('./pic1/'+f)
