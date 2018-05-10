# -*- coding: utf-8 -*-
import scrapy
from hao6v.items import Hao6VItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider
from scrapy.spider import Rule

class Hao6vSpider(CrawlSpider):
    name = 'hao6V'
    allowed_domains = ['hao6v.com']
    start_urls = ['http://www.hao6v.com/gydy/']
    pagelink = LinkExtractor(restrict_xpaths='//div[@class="listpage"]', allow=r'index_\w+.html')

    rules = [
        Rule(pagelink, callback = "parsePage", follow = True)
    ]

    def parsePage(self, response):
        # cards = response.xpath('//ul[@class="list"]//a')
        item = Hao6VItem()
        for each in response.xpath('//ul[@class="list"]/li//a'):
            if each.xpath('./text()'):
                # item['movie_name'] = each.xpath('./text()').extract()
                detail_url = each.xpath('./@href').extract()[0]
                yield scrapy.Request(detail_url,callback=self.parseDetail)

    def parseDetail(self,response):











