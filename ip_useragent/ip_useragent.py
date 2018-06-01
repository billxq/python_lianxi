#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/21 下午12:24
# @author: Bill
# @file: ip_useragent.py

import random
from multiprocessing import Process
from lxml import html
import requests

# -------------------------------------------------------文档处理----------------------------------------------------
def writeFile(path,text):
    with open(path,'a',encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n')

def truncatefiles(path):
    with open(path,'w',encoding='utf-8') as f:
        f.truncate()

def readFile(path):
    ip_list = list()
    with open(path,'r',encoding='utf-8') as f:
        for s in f.readlines():
            ip_list.append(s)
    return ip_list

# -------------------------------------------------------获取随机的请求头headers----------------------------------------------------

def getHeaders():
    useragent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    user_agent = random.choice(useragent_list)
    headers = {
        "User-Agent": user_agent
    }
    return headers

# -------------------------------------------------------判断代理ip的可用性----------------------------------------------------
def checkAlive(ip):
    try:
        session = requests.session()
        headers = getHeaders()
        url = 'https://www.baidu.com'
        proxies = {"http": "http://" + ip, "https": "http://" + ip}
        r = session.get(url,proxies=proxies,timeout=5).status_code
        if r == 200:
            return True
        else:
            return False
    except:
        return False

# -------------------------------------------------------获取代理方法----------------------------------------------------
def findIps(type,pagenum):
    url_list = {'1': 'http://www.xicidaili.com/nt/', # xicidaili国内普通代理
                  '2': 'http://www.xicidaili.com/nn/', # xicidaili国内高匿代理
                  '3': 'http://www.xicidaili.com/wn/', # xicidaili国内https代理
                  '4': 'http://www.xicidaili.com/wt/'} # xicidaili国外http代理
    url = url_list[str(type)] + str(pagenum)
    session = requests.session()
    headers = getHeaders()
    res = session.get(url,headers=headers,timeout=5)
    tree = html.fromstring(res.text)
    cards = tree.xpath('//table[@id="ip_list"]/tr[@class]')
    for each in cards:
        ip = each.xpath('./td[2]/text()')[0]
        port = each.xpath('./td[3]/text()')[0]
        proxy_ip = ip + ':' + port
        if checkAlive(proxy_ip):
            writeFile('./iplist.txt',proxy_ip)


# -------------------------------------------------------多进程获取ip----------------------------------------------------
def getIp():
    p1 = Process(target=findIps,args=(1,1,))
    p2 = Process(target=findIps,args=(1,2,))
    p3 = Process(target=findIps,args=(1,3,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("End!")



if __name__ == '__main__':
    getIp()















