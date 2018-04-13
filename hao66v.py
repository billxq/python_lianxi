#!/usr/bin/env python
# coding:utf-8
import json
import re

import requests


class GetHao6v(object):
    def __init__(self):
        self.indexes = list()
        self.result = dict()
    def get_all_index(self,url):
        res = requests.get(url).text
        max_pag_pat = re.compile(r'class="listpage">.*?<b>(.*?)</b>')
        max_pag = re.findall(max_pag_pat,res)[0].split('/')[1]
        self.indexes = [url] + ['{}index_{}.html'.format(url,i) for i in range(2,int(max_pag)+1)]
        return self.indexes
    def parse_page(self,url):
        res = requests.get(url).text
        patt = re.compile(r'<ul class="list">(.*?)</ul>',re.S)
        url_text = patt.findall(res)[0]
        url_patt = re.compile(r'''<li.*?href="(.*?)" target''')
        url_list = url_patt.findall(url_text)
        return url_list

    def get_details(self,url):
        res = requests.get(url)
        res.encoding= res.apparent_encoding
        title_pat = re.compile(r'<h1>(.*?)</h1>')
        ed2k_pat = re.compile(r'(ed2k.*/)"')
        mag_pat = re.compile(r'(magnet.*)"')
        title = re.findall(title_pat,res.text)
        ed2k = re.findall(ed2k_pat,res.text)
        mag = re.findall(mag_pat,res.text)
        yield {
            "title": title[0].strip(),
            "ed2k":ed2k,
            "magnet":mag
        }


if __name__ == '__main__':
    url = 'http://www.hao6v.com/dy/'
    gethao6v = GetHao6v()
    for i in gethao6v.get_all_index(url):
        for url in gethao6v.parse_page(i):
            for items in gethao6v.get_details(url):
                with open('film.txt','a',encoding='utf-8') as f:
                    f.write(json.dumps(items,ensure_ascii=False) + '\n')
                    f.close()



