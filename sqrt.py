#!/usr/bin/env python
# coding:utf-8
import math

# ax^2 + bx + c = 0

def quaderatic(a,b,c):
    argv = [a,b,c]
    for i in argv:
        if not isinstance(i,(str,int)):
            raise TypeError("bad type")
    delta = b*b -4*a*c
    if delta == 0:
        return -b/(2*a)
    elif delta > 0:
        return (-b + math.sqrt(delta))/2*a, (-b - math.sqrt(delta))/2*a
    else:
        return None


print(quaderatic(1,6,3))
        
