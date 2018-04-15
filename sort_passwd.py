#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/15 下午7:34
# @author: Bill
# @file: demon1

with open('/etc/passwd','r') as f:
    result = sorted(f.readlines(),key=lambda item:int(item.split(':')[2]))

with open('./1.txt','w') as f:
    f.writelines(result)
