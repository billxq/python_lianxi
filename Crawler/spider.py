#!/usr/bin/env python
# coding:utf-8


from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider(object):

    # shared information
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self,project_name,base_url,domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page("First_page",base_url)

    # Creates directory and files for the project on first run and start the spider

    @staticmethod
    def boot():

