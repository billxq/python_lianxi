#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/14 上午9:39
# @author: Bill
# @file: jiepai.py
import os
from hashlib import md5
import requests
from urllib.parse import urlencode
import re
from pyquery import PyQuery as pq
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer":"https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D%E7%BE%8E%E5%A5%B3"
}

def getPage(offset):
    params = {
        "offset": "offset",
        "keyword": "街拍美女",
        "autoload": "true",
        "count": 20,
        "cur_tab": 1,
        "format":"json"
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            return res.json()
    except requests.ConnectionError as e:
        return None

def saveImages(item,url):
    path = './街拍美图/' + item.get('title')
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        res = requests.get(url)
        if res.status_code == 200:
            file_path = f'{path}/{md5(res.content).hexdigest()}.jpg'
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(res.content)
            else:
                print("Already Downloaded!",file_path)
    except requests.ConnectionError:
        print("Error!")



def parsePage(json):
    if json:
        items = json['data']
        for item in items:
            if 'title' in item.keys():
                title = item['title']
                print("开始下载",title)
            if 'image_list' in item.keys():
                for pic in item['image_list']:
                    pic_string = pic['url'][2:]
                    real_url = 'http://' + re.sub('list','large',pic_string)
                    saveImages(item,real_url)



if __name__ == '__main__':
    json = getPage(10)
    parsePage(json)
