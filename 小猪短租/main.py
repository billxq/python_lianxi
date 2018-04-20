#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/19 下午11:59
# @author: Bill
# @file: main.py

'''
爬取小猪短租网上，上海青浦区徐泾东的租房信息
首页地址是：http://sh.xiaozhu.com/%E5%BE%90%E6%B3%BE%E4%B8%9C_uw2a6d-duanzufang-20/?putkey=%E5%BE%90%E6%B3%BE%E4%B8%9C
'''

import requests
import re

class XiaoZhu(object):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
               }
    def __init__(self):
        print("初始化中...")
        print("这个类的作用:爬取小猪短租网上，上海青浦区徐泾东的租房信息")

    def getResponse(self,url):
        res = requests.get(url,headers=self.headers)
        if res.status_code == 200:
            return res
        return None

    def getDetails(self,url):
        res = self.getResponse(url)
        patt = re.compile(r'''class="result_price">.*?<i>(.*?)</i>.*?"search_result_gridsum" href="(.*?)" target=.*?'''
                          + '''hiddenTxt">(.*?)</span>.*?"hiddenTxt">(.*?)<span class="commenthref">(.*?)</span>''',
                          re.S)
        results = re.findall(patt,res.text)
        for result in results:
            yield {
                "title":result[2],
                "price":result[0],
                "url":result[1],
                "type":result[3].replace('\n',' ').strip().split('-')[1].lstrip(),
                "rating":result[4].replace('\n',' ').strip().split('-')[1]
            }


def main():
    url = 'http://sh.xiaozhu.com/%E5%BE%90%E6%B3%BE%E4%B8%9C_uw2a6d-duanzufang-20/?putkey=%E5%BE%90%E6%B3%BE%E4%B8%9C'
    xiaozhu = XiaoZhu()
    for item in xiaozhu.getDetails(url):
        print(item)


if __name__ == '__main__':
    main()

