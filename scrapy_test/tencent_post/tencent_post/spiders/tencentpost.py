# -*- coding: utf-8 -*-
import scrapy


class TencentpostSpider(scrapy.Spider):
    name = 'tencentpost'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        postion_cards = response.xpath('//tr[(@class="even" or @class="odd")]')
        for card in postion_cards:
            postion = card.xpath('./td[@class="l square"]/a/text()')[0].extract()
            print(postion)

