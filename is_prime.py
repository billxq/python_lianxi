#!/usr/bin/env python
# coding:utf-8

import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_prime1(n):
    
