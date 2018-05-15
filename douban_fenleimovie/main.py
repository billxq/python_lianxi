#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/15 上午10:29
# @author: Bill
# @file: main.py
import csv
import os
from urllib.parse import urlencode
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Host": "movie.douban.com",
    "Referer": "https://movie.douban.com/tag/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}



def getPage(start):
    parms = {
        "sort": "T",
        "range": "0, 10",
        "start": start,
        "genres": "犯罪"
    }
    url = 'https://movie.douban.com/j/new_search_subjects?' + urlencode(parms)
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            return res.json()
        else:
            return None
    except requests.ConnectionError:
        print("Url Request error!")



def parsePage(json):
    items = json['data']
    for item in items:
        yield {
            "title": item['title'],
            "url": item['url'],
            "directors": "".join(item['directors']),
            "casts": "".join(item['casts']),
            "rate": item['rate'],
            "star": item['star']
        }




def saveToCsv(result):
    file = './movie.csv'
    if not os.path.isfile(file):
        with open('./movie.csv','w') as f:
            fieldnames = ['title','url','directors','casts','rate','star']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(result)
    else:
        with open('./movie.csv','a') as f:
            fieldnames = ['title','url','directors','casts','rate','star']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerow(result)


if __name__ == '__main__':
    for start in range(0,10001,20):  # 不知道最大多少页，所以设了一个很大的值，然后判断网页返回是否为None来做判断
        json = getPage(start)
        if json:
            results = parsePage(json)
            for result in results:
                saveToCsv(result)
