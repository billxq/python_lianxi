#!usr/bin/env python  
# coding:utf-8
""" 
@author:xuqing 
@file: no_same_digit.py 
@time: 2018/06/26 
"""

'''题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位
数？都是多少？'''

l1 = list()

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b!=c:
                num = str(a)+str(b)+str(c)
                l1.append(num)


print("一共有{}个不重复的三位数".format(len(l1)))
print("他们是：")
for i in l1:
    print(i)