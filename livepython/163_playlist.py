#!/usr/bin/env python
# coding:utf-8
# @author: Bill

"""
爬取网易云音乐歌单播放数超过500w的歌单，存入csv文件中，文件名自己在write_csv函数中指定
"""

import csv
import os
import requests
import re
import time

header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer":"http://music.163.com",
    "Cookie":"__f_=1524827065935; _ntes_nnid=5f658c7c56fe6e24aa3f1e138c033b6a,1524827066031; _ntes_nuid=5f658c7c56fe6e24aa3f1e138c033b6a; _iuqxldmzr_=32; __utmz=94650624.1525078730.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=%2FDC384g5qTeak08YocVD2Kf57WEDFb0F; __remember_me=true; __utma=94650624.894094420.1525078730.1525086489.1525270917.3; __utmc=94650624; JSESSIONID-WYYY=Dp7qTBxv6D1oOC3ZR4952rblv%2BPq%5CKuk4dfxMcflKbyldfSq1S5R7Aqmll1C66f%2Bj469%5Cue%2FY6ZiP%2F%2ByOeqT%5CxrIqnZSMM478%2F66H5ZO%2FAOQB2Kmlt93z9UzBNHnbSxQYcE90YPsPCQsSSbAzMrTuUBqTPQEQBgsRH809IZO1OcpbMRr%3A1525274457491; MUSIC_U=71ce523a8795b31f99820c550e646a13a3af3a7ad30b39bdcf621e6ff5855f1f804856c3e63af58a81171b596ee7d8baffddc004a62cd46ac3061cd18d77b7a0; __csrf=a599e86daa966dc6d9a33b17d383ebc9; __utmb=94650624.20.10.1525270917"
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






