#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/25 下午1:03
# @author: Bill
# @file: spy_on_weibo.py

from selenium import webdriver
import time

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    return driver

def wb_login(name,password):
    print('准备登陆微博')
    try:
        driver = start_chrome()
        driver.get('https://weibo.com')
        driver.implicitly_wait(10)
        ele_name = driver.find_element_by_id('loginname')
        ele_name.send_keys(name)
        time.sleep(2)
        ele_pwd = driver.find_element_by_name('password')
        ele_pwd.send_keys(password)
        time.sleep(2)
        driver.find_element_by_css_selector('#pl_login_form > div > div:nth-child(3) > div.info_list.login_btn > a').click()
        return driver
    except Exception as e:
        print(e)

if __name__ == '__main__':
    driver = wb_login()
    ele_text = driver.find_element_by_css_selector('#v6_pl_content_publishertop > div > div.input > textarea')
    text = '你好，这是我用selenium发的微博！Hello world,hello python!'
    ele_text.send_keys(text)
    time.sleep(2)
    driver.find_element_by_css_selector('#v6_pl_content_publishertop > div > div.func_area.clearfix > div.func > a').click()





