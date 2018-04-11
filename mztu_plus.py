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
        try:
            res = requests.get(self.index_url,headers=self.headers).text
            set_urls_pattern = re.compile(r'http://www.mzitu.com/\d+')
            self.set_urls_list = set_urls_pattern.findall(res)
            return self.set_urls_list
        except Exception as e:
            print(e)
            
    def get_single_set_pages(self,url):
        pic_url = list()
        try:
            res = requests.get(url,headers=self.headers).text
            title_pattern = re.compile(r'<h2 class="main-title">(.*?)</h2>')
            max_page_number = re.findall(r"<span class='dots'>.*?</span>.*?href='.*?'><span>(.*?)<",res)[0]
            self.title = title_pattern.findall(res)[0].strip()
            single_set_pages = ['{}/{}'.format(url,i) for i in range(1,int(max_page_number)+1)]
            for page in single_set_pages:
                res = requests.get(page,headers=self.headers)
                real_pic_url = re.findall(r'<img src="(.*?)" alt',res.text)
                pic_url.append(real_pic_url[0])
            return pic_url
        except Exception as e:
            print(e)
    def download_set_pics(self,pic_url):
        set_dir = self.title
        if not os.path.exists(set_dir):
            os.mkdir(set_dir)
        try:
            content = requests.get(pic_url,headers=self.headers).content
            path = './{}/{}.{}'.format(set_dir,md5(content).hexdigest(),'jpg')
            with open(path,'wb') as f:
                f.write(content)
            print("{}  已下载".format(pic_url))
        except Exception as e:
            print(e)
    def judge_dir(self):
        files = os.listdir('./')
        if self.title in files:
            print("套图已存在！无需下载！")
            return True
        return False

if __name__ == "__main__":
    getmeizitu = GetMeiZiTu(url)
    for single_sets in getmeizitu.get_all_sets():
        if not getmeizitu.judge_dir():
            for pic_url in getmeizitu.get_single_set_pages(single_sets):
                getmeizitu.download_set_pics(pic_url)
            time.sleep(5)
            print(getmeizitu.title + "套图已下载！等待5秒进入下一套图的下载！")
















