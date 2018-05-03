#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/3 下午2:12
# @author: Bill
# @file: douban_movie_top250.py
import csv
import requests
from bs4 import BeautifulSoup


def q(num):
    return f'https://movie.douban.com/top250?start={num}'

def main(url):
    try:
        r = requests.get(url).text
        soup = BeautifulSoup(r,'lxml')
        name_patt = soup.select('div.hd > a > span:nth-of-type(1)')
        actor_patt = soup.select('div.bd > p:nth-of-type(1)')
        for name,actor in zip(name_patt,actor_patt):
            patt = actor.get_text().replace(' ','').replace('\n','').split('...')[0].split()
            director = patt[0][3:]
            actor = patt[1][3:]
            with open('./movie_top250.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([name.get_text(),director,actor])
            print(f'{name.get_text()} done!')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    with open('./movie_top250.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['片名', '导演', '主演'])
    for i in range(0,226,25):
        main(q(i))