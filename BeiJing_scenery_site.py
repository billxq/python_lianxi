#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import requests
import pymysql

def db_connect():
    db_data = {
        "host":"192.168.80.130",
        "port":3306,
        "user":"python",
        "passwd":"123456",
        "db":"python",
        "charset":"utf8"
    }
    db = pymysql.connect(**db_data)
    return db

class GetCtrip(object):
    def __init__(self):
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
        }
    def get_response(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = res.apparent_encoding
        if res.status_code == 200:
            return res
        return None
    def get_details(self,url):
        res = self.get_response(url)
        patt = re.compile(r'''"search_ticket_title">.*?title">(.*?)</a>.*?adress">(.*?)</div>.*?exercise">(.*?)</div>.*?<em>(.*?)</em>''',re.S)
        results = re.findall(patt,res.text)
        for result in results:
            yield {
                "place":result[0].split()[0].replace('\\',''),
                "address":result[1].split()[0],
                "exercise":result[2].split(),
                "rating":result[3].split()[0]
            }


if __name__ == '__main__':
    getctrip = GetCtrip()
    db = db_connect()
    cur = db.cursor()
    cur.execute('CREATE TABLE  IF NOT EXISTS XIECHENG(PLACE CHAR(40),ADDRESS CHAR(40),EXERCISE CHAR(100),RATING CHAR(10))ENGINE=INNODB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1')
    urls = ['http://piao.ctrip.com/dest/u-_b1_b1_be_a9/s-tickets/P{}'.format(str(i)) for i in range(1,45)]
    for url in urls:
        for item in getctrip.get_details(url):
            sql = """INSERT INTO XIECHENG(PLACE,ADDRESS,EXERCISE,RATING)VALUES("{}","{}","{}","{}")""".format(item['place'],item['address'],item['exercise'],item['rating'])
            try:
                cur.execute(sql)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
    db.close()


