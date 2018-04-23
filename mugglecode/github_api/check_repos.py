#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/23 上午10:00
# @author: Bill
# @file: check_repos.py

"""
输入要比对的库名和生态topic
比对各个库的star数，forks数和topic的totalcount数
"""

import requests

def get_names():
    names = input("请输入库名和topic名（用空格分开）：")
    return names.split()

def check_repos(names):
    ecosys_api = 'https://api.github.com/search/repositories?q=topic:'
    repo_api = 'https://api.github.com/search/repositories?q='
    for name in names:
        repo_info = requests.get(repo_api+name).json()['items'][0]
        stars = repo_info['stargazers_count']
        forks = repo_info['forks_count']
        ecosys_info = requests.get(ecosys_api + name).json()['total_count']

        print(name)
        print('Stars:'+str(stars))
        print('Forks:'+str(forks))
        print('Ecosys:'+str(ecosys_info))
        print('----------')

names = get_names()
check_repos(names)