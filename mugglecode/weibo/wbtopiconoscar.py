#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/28 下午1:58
# @author: Bill
# @file: wbtopiconoscar.py
from selenium import webdriver 


def startChrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    return driver

def get_info(url):
    driver = startChrome()
    driver.get(url)
    driver.implicitly_wait(10)
    sel = '#pl_common_searchTop > div.search_topic > div.m_topic > div.small_pic > div > p > span:nth-child(2)'
    result = driver.find_element_by_css_selector(sel).text
    return result.replace("讨论","")

if __name__ == '__main__':
    url = "https://s.weibo.com/weibo/%2523%25E5%25A5%25A5%25E6%2596%25AF%25E5%258D%25A1%2523&Refer=STopic_box"
    target = "360万"
    current = get_info(url)
    if current > target:
        print(f'讨论数超过目标{target}，为{current}')
    else:
        print(f'讨论数未超过目标{target}')