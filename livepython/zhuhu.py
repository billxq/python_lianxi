#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/4 上午9:33
# @author: Bill
# @file: zhuhu.py
import time

import requests
import pandas as pd

user_data = list()
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Referer":"https://www.zhihu.com/people/excited-vczh/following",
    "Cookie":'''请自行填入'''
}

def q(offset):
    return f'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={offset}&limit=20'

def get_page(url):
    followee_dict = requests.get(url,headers=headers).json()['data']
    user_data.extend(followee_dict)



if __name__ == '__main__':
    for i in range(10):     # 第一页的offset值是0，所以i从0开始，这里选择爬取10页followee信息
        get_page(q(20*i))
        df = pd.DataFrame(user_data)
        df.to_csv('user_data.csv')
        time.sleep(2)