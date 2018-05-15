#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/15 上午10:29
# @author: Bill
# @file: main.py
import csv
import os
import time
from urllib.parse import urlencode
import requests
from multiprocessing import Pool,cpu_count

headers = {
    "Accept": "application/json, text/plain, */*",
    "Host": "movie.douban.com",
    "Referer": "https://movie.douban.com/tag/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}



def getPage(start,genres):
    parms = {
        "sort": "T",
        "range": "0, 10",
        "start": start,
        "genres": genres
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


def saveToCsv(result,genres):
    file = './movie_{}.csv'.format(genres)
    if not os.path.isfile(file):
        with open(file,'w') as f:
            fieldnames = ['title','url','directors','casts','rate','star']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(result)
    else:
        with open(file,'a') as f:
            fieldnames = ['title','url','directors','casts','rate','star']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerow(result)


def main(genres):
    print("Getting info from {}".format(genres))
    for start in range(0,101,20):  # 不知道最大多少页，所以设了一个很大的值，然后判断网页返回是否为None来做判断
        if start == 0:
            page = 1
        page = start / 20
        json = getPage(start,genres)
        if not json:
            exit(1)
        else:
            results = parsePage(json)
            for result in results:
                saveToCsv(result,genres)
            print("Writing Page {}".format(int(page)+1))
            time.sleep(1)

if __name__ == '__main__':
    Genres_list = ["剧情", "喜剧", "动作", "爱情", "科幻", "悬疑", "惊悚", "恐怖", "犯罪", "同性", "音乐", "歌舞", "传记", "历史", "战争", "西部", "奇幻",
                   "冒险", "灾难", "武侠", "情色"]
    pool = Pool(processes=cpu_count())
    pool.map(main,Genres_list)