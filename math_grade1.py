#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/25 上午8:55
# @author: Bill
# @file: math_grade1.py
'''
一年级数学题：
上学 + 学上 = 学学好
'''
for x in range(1,10):
    for y in range(10):
        for z in range(10):
            a = 10 * x + y
            b = 10 * y + x
            c = 100 * y + 10 * y + z
            if a + b == c:
                print(f'   {x} {y}\n',
                      f'+ {y} {x}\n',
                    '———————————————\n',
                      f'{y} {y} {z}')