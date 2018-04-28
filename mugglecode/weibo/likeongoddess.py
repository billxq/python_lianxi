#!/usr/bin/env python
# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def login(driver,url):
    driver.get(url)
    time.sleep(25)


def scrollDown():
    sel = 'html'
    html_tag = driver.find_element_by_tag_name(sel)
    for i in range(5):
        print(i)
        html_tag.send_keys(Keys.END)
        time.sleep(0.8)




def clickLike(driver,url,have_clicked):
    driver.get(url)
    time.sleep(6)
    scrollDown()
    time.sleep(8)
    card_sel = "#Pl_Official_MyProfileFeed__20 > div > div"
    cards = driver.find_elements_by_css_selector(card_sel)
    for card in cards:
        time_sel = 'div.WB_detail > div.WB_from.S_txt2 > a.S_txt2:nth-child(1)'
        weibo_time = card.find_elements_by_css_selector(time_sel)
        if len(weibo_time) == 1:
            weibo_time = weibo_time[0].text
        if weibo_time not in have_clicked:
            like_sel = 'div.WB_feed_handle > div > ul > li:nth-child(4) > a > span > span > span > em.W_ficon.ficon_praised.S_txt2'
            like = card.find_elements_by_css_selector(like_sel)
            if len(like) == 1:
                like = like[0]
                try:
                    like.click()
                except Exception:
                    html_page = driver.find_element_by_tag_name('html')
                    html_page.send_keys(Keys.DOWN)
                    like.click()
                have_clicked.append(weibo_time)
                time.sleep(5)






if __name__ == '__main__':
    have_clicked = list()
    base_url = 'https://weibo.com'
    url = "https://weibo.com/u/6436711340?topnav=1&wvr=6&topsug=1&is_hot=1#_rnd1524916989910"
    driver = start_chrome()
    login(driver,base_url)
    while 1:
        have_clicked = clickLike(driver,url,have_clicked)
        print(have_clicked)
        time.sleep(1200)

#
# driver = start_chrome()
# url = "https://weibo.com/u/6436711340?topnav=1&wvr=6&topsug=1&is_hot=1#_rnd1524916989910"
# driver.get(url)
# time.sleep(5)
# scrollDown()
# time.sleep(10)
# card_sel = "div.WB_feed_detail"
# cards = driver.find_elements_by_css_selector(card_sel)
# for card in cards:
#     time_sel = 'div.WB_detail > div.WB_from.S_txt2 > a.S_txt2:nth-child(1)'
#     weibo_time = card.find_elements_by_css_selector(time_sel)
#     like_sel = '#Pl_Official_MyProfileFeed__20 > div > div:nth-child(2) > div.WB_feed_handle > div > ul > li:nth-child(4) > a > span > span'
#     like = card.find_elements_by_css_selector(like_sel)
#     print(weibo_time,like)