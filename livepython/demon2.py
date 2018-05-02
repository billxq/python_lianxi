#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/2 下午12:23
# @author: Bill
# @file: demon2.py
import csv
import os
import redis
'''
将redis数据库里的数据写入csv文件
'''

pool = redis.ConnectionPool(host="10.211.55.4",port=6379,db=0)
r = redis.Redis(connection_pool=pool)

def write_csv(file_path,content):
    fieldnames = ('id','name','address','image_url','price','score','url')
    if not os.path.exists(file_path):
        with open(file_path,'w',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            writer.writerow(content)
    else:
        with open(file_path,'a',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(content)          


for k in r.keys():
    # write_csv('./hotel_info.csv',[i.decode('utf-8') for i in r.hgetall(k)])
    # id,name,address,image_url,price,score,url = r.hmget(k,'id','name','address','image_url','price','score','url')
    # write_csv('./hotel_info.csv',(r.hmget(k,'id','name','address','image_url','price','score','url')))
    write_csv('./hotel_url.csv',list(map(lambda x:x.decode('utf-8'),r.hmget(k,'id','name','address','image_url','price','score','url'))))