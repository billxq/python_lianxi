# -*- coding: utf-8 -*-
import scrapy
from hao6v.items import Hao6VItem

class Hao6vSpider(scrapy.Spider):
    name = 'hao6V'
    allowed_domains = ['hao6v.com']
    offset = 2
    start_urls = ['http://www.hao6v.com/gydy/']


    def parse(self, response):
        cards = response.xpath('//ul[@class="list"]//a')
        for each in cards:
            item = Hao6VItem()
            if each.xpath('./@href').re('http://www.hao6v.com/\S+?/\S+?/\S+?html'):
                item['movie_name'] = each.xpath('./text()').extract()
                item['movie_url'] = each.xpath('./@href').re('http://www.hao6v.com/\S+?html')[0]
                yield item
        if self.offset <= 66:
            self.offset += 1
            next_url = self.start_urls[0] + f'index_{self.offset}.html'
        yield scrapy.Request(next_url,callback=self.parse)





