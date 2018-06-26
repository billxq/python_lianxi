#!usr/bin/env python  
# coding:utf-8
""" 
@author:xuqing 
@file: 3.py 
@time: 2018/06/26 
"""

'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全
平方数，请问该数是多少？
'''
import math
i = 0
while i<10000:
    n1 = i + 168
    n2 = i + 268
    result1 = math.sqrt(n1)
    result2 = math.sqrt(n2)
    if (math.floor(result1)**2 == n1) and (math.floor(result2)**2 == n2):
        print(i)
    i += 1

