#!/usr/bin/env python
# coding:utf-8
# @author: Bill

"""
爬取网易云音乐歌单播放数超过500w的歌单，存入csv文件中，文件名自己在write_csv函数中指定
cookie需要自己指定，否则无法验证登录状态
"""

import csv
import os
import requests
import re
import time

header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer":"http://music.163.com",
    "Cookie":""
}

# offset的值是35的倍数，每页显示35个歌单
def q(offset):
    return f'http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset={offset}'



def get_detail(url):
    try:
        r = requests.get(url,headers=header,timeout=10).text
    except Exception as e:
        print(e)
    pat = re.compile(r'<img class="j-flag".*?title="(.*?)" href="(.*?)" class="msk".*?class="nb">(.*?)</span>',re.S)
    results = re.findall(pat,r)
    for result in results:
        yield {
            "title":result[0],
            "playlist_url": "http://music.163.com" + result[1],
            "play_count":result[2]
        }


def write_csv(file_path,content):
    if not os.path.exists(file_path):
        with open(file_path,'w',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['歌单','歌单地址','播放次数'])
    else:
        with open(file_path,'a',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(content)


if __name__ == '__main__':
    page = 1
    for i in range(0,1261,35):
        results = get_detail(q(i))
        for result in results:
            if result['play_count'].endswith('万') and int(result['play_count'].replace("万","")) >= 500:
                content = [result['title'],result['playlist_url'],result['play_count']]
                # write_csv('./网易播放500万+歌单.csv',content)
                print(content)
        print(f'第{page}写入成功！休眠2秒！')
        page += 1
        time.sleep(2)






