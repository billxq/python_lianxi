#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/25 下午5:41
# @author: Bill
# @file: test.py

import requests
import re
url = 'http://www.kugou.com/yy/html/rank.html'

def get_top(url):
    info = {}
    res = requests.get(url).text
    patt = re.compile(r'<li class=" " title="(.*?)" data-index',re.S)
    results = re.findall(patt,res)
    for result in results:
        singer = result.split('-')[0]
        song = result.split('-')[1]
        info.update({singer:song})
    return info

if __name__ == '__main__':
    for k,v in get_top(url).items():
        print(f'singer:{k}',
              f'song:{v}')