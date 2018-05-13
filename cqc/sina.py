#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/13 下午10:29
# @author: Bill
# @file: sina.py

import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

def getPage(page):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Cookie":"_T_WM=407dedcab3c6fcfa23232f5f81ea4a5e; ALF=1528813953; SCF=AlAY5lTLsRzpRrZAY3bZ__w6y7NEjPHRhgPhJMwy5rCNdjn9r6oOeXFQIs2AF_81oe0BFjHj04tj_Z1DYJUa_kE.; SUB=_2A253_D3hDeRhGeRK7FQX8SvEyziIHXVVH0OprDV6PUJbktAKLRD3kW1NU3YWyicYqwJPCFf_g0FuJ8t7Cj6PgZh3; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWBXKjB5YoqbQiSyJVcELe15JpX5K-hUgL.FozXS0qceK-RehB2dJLoIpjLxKnLB-qL1K2LxKqLBonL1h-LxK.LBKeL12-t; SUHB=0YhgbdQPktKMS3; SSOLoginState=1526222257; H5_INDEX_TITLE=%E8%AF%91%E6%B8%85%E9%A3%8E; H5_INDEX=2; h5_deviceID=34638a50e7709ba34430b997893a7aff; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E5%2586%25AF%25E6%258F%2590%25E8%258E%25AB%2526t%253D10%26featurecode%3D20000320%26fid%3D1076031672384324%26uicode%3D10000011",
        "X-Requested-With": "XMLHttpRequest",
        "Host": "m.weibo.cn",
        "Referer": "https://m.weibo.cn/u/1672384324"
    }
    data = {
        "uid": 1672384324,
        "luicode": 10000011,
        "lfid": "100103type=1&q=冯提莫&t=10",
        "featurecode": 20000320,
        "type": "uid",
        "value": 1672384324,
        "containerid": 1076031672384324,
        "page": page
    }
    request_url = 'https://m.weibo.cn/api/container/getIndex?' + urlencode(data)
    res = requests.get(request_url,headers=headers).json()
    return res


def parse_page(json):
    if json:
        items = json['data']['cards']
        for item in items:
            if "mblog" in item.keys():
                item = item['mblog']
                text = pq(item['text']).text()  # 借助pyquery将正文中的html标签去掉
                print(text)

if __name__ == '__main__':
    for page in range(1,10):
        json = getPage(page)
        parse_page(json)