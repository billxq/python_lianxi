#!/usr/bin/env python
# coding:utf-8
import os
import re
import time

import requests
from bs4 import BeautifulSoup
import re
from hashlib import md5
from multiprocessing import Pool

model_url_list = list()

def getAllPages(url,pn):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
    data = {
        'q': '',
        'viewFlag': 'A',
        'sortType': 'default',
        'searchStyle': '',
        'searchRegion': 'city:',
        'searchFansNum': '',
        'currentPage': pn,
        'pageSize': 100
    }
    res = requests.post(url,headers=headers,data=data)
    res.encoding = res.apparent_encoding
    data =  res.json()['data']['searchDOList']
    for result in data:
        userId = result['userId']
        model_url = f'https://mm.taobao.com/self/aiShow.htm?&userId={userId}'
        model_url_list.append(model_url)

def create_dirs(mm_name):
    if not os.path.exists(mm_name):
        os.makedirs(mm_name+'/'+ mm_name+'_album')
        pic_path = mm_name+'/'+ mm_name+'_album'
    return pic_path

def getInfo(model_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
    res = requests.get(model_url,headers=headers).text
    soup = BeautifulSoup(res,'lxml')
    mm_name = soup.select('dd > a:nth-of-type(1)')[0].get_text()
    pic_path = create_dirs(mm_name)
    for link in soup.find_all('img'):
        if link.get('src').strip() != "":
            pic_url = "http:" + link.get('src').strip()
            save_imgs(pic_url,pic_path)
            print("正在下载：  " + link.get('src').strip())

def save_imgs(pic_url,pic_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
    try:
        content = requests.get(pic_url,headers=headers,timeout=10).content
        with open(pic_path+f'/{md5(content).hexdigest()}.jpg','wb') as f:
            f.write(content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    pool = Pool(processes=2)
    url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
    for pn in range(1,2):
        getAllPages(url,pn)
        print(f'Crawling page {pn} now...')
        time.sleep(1)
    pool.map(getInfo,model_url_list)




# model_url = 'https://mm.taobao.com/self/aiShow.htm?spm=719.7763510.1998643336.1.5FpAsI&userId=176817195'
# getInfo(model_url)