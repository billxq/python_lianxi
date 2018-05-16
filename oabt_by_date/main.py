#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/15 下午2:59
# @author: Bill
# @file: main.py
from datetime import datetime

import requests
from bs4 import BeautifulSoup


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Host": "oabt004.com",
    "Referer": "http://oabt004.com/index/index",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

def getPage(num):
    url = 'http://oabt004.com/index/index/p/{}'.format(num)
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            return res
        return None
    except requests.ConnectionError as e:
        raise e



def parsePage(res):
    t = datetime.today().strftime("%Y-%m-%d")
    soup = BeautifulSoup(res.text,'lxml')
    date_sel = soup.select('p.link-list-title')
    if date_sel:
        date = date_sel[0].get_text().split()[1]
        if date == t:






if __name__ == '__main__':
    t = datetime.today().strftime("%Y-%m-%d")
    date = getDate(getPage(1))
    print(t)
    print(date)