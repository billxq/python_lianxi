#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from hashlib import md5
import requests
import re

import time

url = 'http://www.mzitu.com/all/'


class GetMeiZiTu(object):
    def __init__(self,index_url):
        self.index_url = index_url
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36','Referer':'http://www.mzitu.com'}
        self.set_urls_list = []
        self.title = None
        self.total_sets = list()
    def get_all_sets(self):
        res = requests.get(self.index_url,headers=self.headers).text
        set_urls_pattern = re.compile(r'http://www.mzitu.com/\d+')
        self.set_urls_list = set_urls_pattern.findall(res)
        return self.set_urls_list
    def get_single_set_pages(self,url):
        pic_url = list()
        res = requests.get(url,headers=self.headers).text
        title_pattern = re.compile(r'<h2 class="main-title">(.*?)</h2>')
        max_page_number = re.findall(r"<span class='dots'>.*?</span>.*?href='.*?'><span>(.*?)<",res)[0]
        self.title = title_pattern.findall(res)[0].strip()
        # print(title,max_page_number)
        single_set_pages = ['{}/{}'.format(url,i) for i in range(1,int(max_page_number)+1)]
        for page in single_set_pages:
            res = requests.get(page,headers=self.headers)
            real_pic_url = re.findall(r'<img src="(.*?)" alt',res.text)
            pic_url.append(real_pic_url[0])
            self.total_sets.append(pic_url)
        return pic_url
    def download_set_pics(self,pic_url):
        set_dir = self.title
        if not os.path.exists(set_dir):
            os.mkdir(set_dir)
        content = requests.get(pic_url,headers=self.headers).content
        path = './{}/{}.{}'.format(set_dir,md5(content).hexdigest(),'jpg')
        with open(path,'wb') as f:
            f.write(content)
        print("{}  已下载".format(pic_url))

getmeizitu = GetMeiZiTu(url)
for single_sets in getmeizitu.get_all_sets():
    if getmeizitu.get_single_set_pages(single_sets) in getmeizitu.total_sets:
        print(getmeizitu.title + "此套图已经下载！")
    else:
        for pic_url in getmeizitu.get_single_set_pages(single_sets):
            getmeizitu.download_set_pics(pic_url)
        print(getmeizitu.title + "套图已下载！等待5秒进入下一套图的下载！")
        print()
        time.sleep(5)
