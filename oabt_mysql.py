#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/16 下午10:26
# @author: Bill
# @file: oabt_survey.py
import re
import requests
import pymysql

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



class GetOabt(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    def get_response(self,url):
        res = requests.get(url,headers=self.headers)
        if res.status_code == 200:
            return res
        return None
    def get_details(self,url):
        res = self.get_response(url)
        patt = re.compile(r'''<li data-id=.*?data-magnet="(.*?)" data-ed2k="(.*?)".*?class="name">(.*?)</span>''',re.S)
        results = re.findall(patt,res.text)
        for result in results:
            yield {
                "name":result[2],
                "magnet":result[0],
                "ed2k":result[1]
            }


if __name__ == '__main__':
    url = 'http://oabt004.com/index/index?cid=1'
    db = db_connect()
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS OABT(NAME CHAR(200),
                    MAGNET TEXT(300),
                    ED2K TEXT(300)
                  )ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
                AUTO_INCREMENT=1''')

    getoabt = GetOabt()
    urls = ['http://oabt004.com/index/index/cid/1/p/{}'.format(str(i)) for i in range(1,10)]
    for url in urls:
        for item in getoabt.get_details(url):
            sql = '''INSERT INTO OABT(NAME,MAGNET,ED2K)
                      VALUES("{}","{}","{}")
                  '''.format(item['name'],item['magnet'],item['ed2k'])
            try:
                cur.execute(sql)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
    db.close()

