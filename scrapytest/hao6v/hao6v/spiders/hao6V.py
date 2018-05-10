# -*- coding: utf-8 -*-
import scrapy
from hao6v.items import Hao6VItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider
from scrapy.spider import Rule

class Hao6vSpider(CrawlSpider):
    name = 'hao6V'
    allowed_domains = ['hao6v.com']
    start_urls = ['http://www.hao6v.com/dy/']
    pagelink = LinkExtractor(restrict_xpaths='//div[@class="listpage"]//a[last()-1]', allow=r'index_\w+.html')

    rules = [
        Rule(pagelink, callback = "parsePage", follow = True)
    ]

    def parsePage(self, response):
        # cards = response.xpath('//ul[@class="list"]//a')

        for each in response.xpath('//ul[@class="list"]/li//a'):
            if each.xpath('./text()'):
                # item['movie_name'] = each.xpath('./text()').extract()
                detail_url = each.xpath('./@href').extract()[0]
                yield scrapy.Request(detail_url,callback=self.parseDetail)

    def parseDetail(self,response):
        item = Hao6VItem()
        for each in response.xpath('//div[@class="box"]'):
            if each.xpath('.//h1/text()'):
                item['movie_name'] = each.xpath('.//h1/text()').extract()[0]
                if each.xpath('.//table//tr//td//a/@href').re('(magnet:.*)'):
                    item['movie_url'] = each.xpath('.//table//tr//td//a/@href').re('(magnet:.*)')[0]
                    yield item
                elif each.xpath('.//table//tr//td//a/@href').re('(ed2k:.*)'):
                    item['movie_url'] = each.xpath('.//table//tr//td//a/@href').re('(ed2k:.*)')[0]
                    yield item
                elif each.xpath('.//table//tr//td//a/@href'):
                    item['movie_url'] = each.xpath('.//table//tr//td//a/@href').extract()[0]
                else:
                    item['movie_url'] = None









