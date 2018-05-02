#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/2 上午9:26
# @author: Bill
# @file: test_redis.py

'''
这个小脚本用于抓取携程网上的纽约名宿酒店信息，并将这些信息写入redis数据库中,以列表形式存储
'''
import time
import redis
import requests

pool = redis.ConnectionPool(host="10.211.55.4",port=6379,db=0)
r = redis.Redis(connection_pool=pool)

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer":"http://hotels.ctrip.com"
}
def get_data(pageIndex):
    data = {
        "cityId": 347,
        "cityPY": "losangeles",
        "checkIn": "2018-05-01",
        "checkOut": "2018-05-02",
        "pageIndex": pageIndex
    }
    return data


def get_details(url,data):
    r = requests.post(url,headers=headers,data=data).json() # 返回一个字典
    hotel_list = r['HotelPostionView']  # 找到关于酒店的键值
    for hotel_info in hotel_list:
        hotel_data = {
            "name": hotel_info['name'],
            "address": hotel_info['address'],
            "image_url": hotel_info['img'],
            "price": "¥" + hotel_info['price'],
            "score": hotel_info['score'],
            "url": "http://hotels.ctrip.com" + hotel_info['url']
        }
        yield hotel_data

if __name__ == '__main__':
    url = 'http://hotels.ctrip.com/apartment/Apartment/Ajax/AjaxApartmentList.aspx'
    for i in range(1,10):
        data = get_data(i)
        results = get_details(url,data)
        for result in results:
            r.lpush("hotel_info",result)
        time.sleep(2)