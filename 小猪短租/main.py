#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/19 下午11:59
# @author: Bill
# @file: main.py

'''
爬取小猪短租网上，上海青浦区徐泾东的租房信息
首页地址是：http://sh.xiaozhu.com/%E5%BE%90%E6%B3%BE%E4%B8%9C_uw2a6d-duanzufang-20/?putkey=%E5%BE%90%E6%B3%BE%E4%B8%9C
'''

import requests
import re
import time
import pymysql

def db_connect():
    db_config = {
        "host": "fishxq.gicp.net",
        "port": 6106,
        "user": "python",
        "passwd": "123456",
        "db": "python",
        "charset":"utf8"
    }
    db = pymysql.connect(**db_config)
    return db

class XiaoZhu(object):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
               }
    def __init__(self):
        print("初始化中...")
        print("这个类的作用:爬取小猪短租网上，上海青浦区徐泾东的租房信息")

    def getResponse(self,url):
        res = requests.get(url,headers=self.headers)
        if res.status_code == 200:
            return res
        return None

    def getDetails(self,url):
        res = self.getResponse(url)
        patt = re.compile(r'''class="result_price">.*?<i>(.*?)</i>.*?"search_result_gridsum" href="(.*?)" target=.*?'''
                          + '''hiddenTxt">(.*?)</span>.*?"hiddenTxt">(.*?)<span class="commenthref">(.*?)</span>''',
                          re.S)
        results = re.findall(patt,res.text)
        for result in results:
            yield {
                "title":result[2],
                "price":int(result[0]),
                "url":result[1],
                "type":result[3].replace('\n',' ').strip().split('-')[1].lstrip(),
                "rating":result[4].replace('\n',' ').strip().split('-')[1]
            }


def main():
    xiaozhu = XiaoZhu()
    db = db_connect()
    cur = db.cursor()
    cur.execute('''create table if not exists Xiaozhu(
                Id int primary key auto_increment,
                Title text not null,
                Price int not null,
                Url text not null,
                Type text not null,
                Rating text not null)ENGINE=INNODB DEFAULT CHARSET=utf8 auto_increment=1
    ''')
    url_list = ['http://sh.xiaozhu.com/%E5%BE%90%E6%B3%BE%E4%B8%9C_uw2a6d-duanzufang-p{}-20/?putkey=%E5%BE%90%E6%B3%BE%E4%B8%9C'.format(str(i)) for i in range(1,10)]
    i = 1
    for url in url_list:
        for item in xiaozhu.getDetails(url):
            sql = '''insert into Xiaozhu(Title,Price,Url,Type,Rating)
                  values("{}","{}","{}","{}","{}")
            '''.format(item['title'],item['price'],item['url'],item['type'],item['rating'])
            try:
                cur.execute(sql)
                db.commit()
                time.sleep(5)
            except Exception as e:
                print(e)
                db.rollback()
        print("Page {} success".format(i))
        i += 1
    db.close()


if __name__ == '__main__':
    # main()
    db = db_connect()
    cur = db.cursor()
    cur.execute('select Title from Xiaozhu;')
    results = cur.fetchall()
    for result in results:
        print(result)