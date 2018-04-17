#!/usr/bin/env python
# coding:utf-8

import re
import requests
import pymysql
import json

def db_connect():
    db_data = {
        "host":"fishxq.gicp.net",
        "port":6106,
        "user":"python",
        "passwd":"123456",
        "db":"python",
        "charset":"utf8"
    }
    db = pymysql.connect(**db_data)
    return db

class GetMaoYan100(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
    def get_response(self,url):
        res = requests.get(url,headers=self.headers)
        if res.status_code == 200:
            return res.text
        else:
            return None
    def get_details(self,url):
        res = self.get_response(url)
        results_pat = re.compile(r'''<p class="name".*?title="(.*?)" data-act.*?class="star">\n(.*?)\n.*?releasetime">(.*?)</p>''',re.S)
        results = re.findall(results_pat,res)
        for result in results:
            yield {
                "title": result[0],
                "actors": result[1].strip()[3:],
                "release-time": result[2][5:]
            }

if __name__ == "__main__":
    urls = ['http://maoyan.com/board/4?offset={}'.format(str(i)) for i in range(0,100,10)]
    getmaoyan100 = GetMaoYan100()
    db = db_connect()
    cur = db.cursor()
    sql = """create table if not exists Maoyan(Title char(40),
             Actors char(40),
            Releasetime char(40)) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
            AUTO_INCREMENT=1"""
    cur.execute(sql)
    for url in urls:
        for item in getmaoyan100.get_details(url):
            sql1 = '''INSERT INTO Maoyan(Title,Actors,Releasetime)
                      VALUES("{}","{}","{}")'''.format(item['title'],item['actors'],item['release-time'])
            try:
                cur.execute(sql1)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
    db.close()
