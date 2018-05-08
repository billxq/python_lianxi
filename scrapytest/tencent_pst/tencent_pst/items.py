# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentPstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post = scrapy.Field()
    post_url = scrapy.Field()
    job_type = scrapy.Field()
    ppl_recru = scrapy.Field()
    place = scrapy.Field()
    post_date = scrapy.Field()
