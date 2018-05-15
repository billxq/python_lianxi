#!/usr/bin/env python
# coding:utf-8
import csv
import os

import time
from selenium import webdriver

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def get_details(driver):
    cards = driver.find_elements_by_css_selector('div.WB_cardwrap.S_bg2.clearfix')
    for card in cards:
        if card:
            nick_name = card.find_elements_by_css_selector('dl > div > div:nth-child(3) > div > a ')
            weibo_content = card.find_element_by_css_selector('p.comment_txt')
            weibo_t_url = card.find_element_by_css_selector('div.feed_from.W_textb > a ')
            try:
                weibo_repost = card.find_element_by_css_selector('div.feed_action.clearfix > ul > li:nth-child(2) > a > span > em').text
            except:
                weibo_repost = '0'
            try:
                weibo_comment = card.find_element_by_css_selector('div.feed_action.clearfix > ul > li:nth-child(3) > a > span > em').text
            except:
                weibo_comment = '0'
            try:
                weibo_like = card.find_element_by_css_selector('div.feed_action.clearfix > ul > li:nth-child(4) > a > span > em').text
            except:
                weibo_like = '0'
            yield {
                "昵称": nick_name[0].text,
                "微博地址": weibo_t_url.get_attribute('href'),
                "发布时间": weibo_t_url.text,
                "微博内容": weibo_content.text.replace('\n',''),
                "转发数": weibo_repost,
                "评论数": weibo_comment,
                "点赞数": weibo_like
            }

def write_csv(content,name):
    if not os.path.exists(f'./{name}.csv'):
        with open(f'./{name}.csv','w+',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(("微博昵称", "微博地址", "发布时间", "微博内容", "转发数", "评论数", "点赞数"))
            writer.writerow(content)
    else:
        with open(f'./{name}.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(content)


def q(search_content,today):
    return f'https://s.weibo.com/weibo/{search_content}&xsort=hot&suball=1&timescope=custom:{today}&Refer=g'


def find_next_page(driver):
    try:
        next_page = driver.find_element_by_css_selector('a.page.next.S_txt1.S_line1')
        if next_page:
            return next_page.get_attribute('href')
        else:
            return None
    except:
        print("没有下一页了！")



def main(q_url,name):
    # driver = start_chrome()
    driver.get(q_url)
    driver.implicitly_wait(10)
    for result in get_details(driver):
        write_csv((v for v in result.values()),name)
    time.sleep(5)
    if find_next_page(driver):
        return main(find_next_page(driver))
    else:
        print(u"没有下一页，程序结束！")
        exit(1)






if __name__ == '__main__':
    # q_url = 'https://s.weibo.com/weibo/%25E8%25BF%25AA%25E4%25B8%25BD%25E7%2583%25AD%25E5%25B7%25B4&xsort=hot&suball=1&timescope=custom:2018-05-01:2018-05-01&Refer=g'
    login_url = 'https://weibo.com'
    driver = start_chrome()
    driver.get(login_url)
    time.sleep(20)
    q_url = q("杨幂","2018-05-01:2018-05-01")
    main(q_url,"杨幂")

