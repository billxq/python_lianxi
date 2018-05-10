# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meitulu.items import MeituluItem


class MeituluSpider(CrawlSpider):
    title = ''
    urllist = list()
    name = 'Meitulu'
    allowed_domains = ['www.meitulu.com']
    start_urls = ['https://www.meitulu.com/t/toutiaonvshen/']

    pagelink = LinkExtractor(restrict_xpaths='//div[@id="pages"]//a[last()]',allow=r'/\w+.html')
    rules = [
        Rule(pagelink, callback = "parse_picset_url", follow=True)
    ]


    def parse_picset_url(self, response):
        for each in response.xpath('//div[@class="boxs"]'):
            set_urls = each.xpath('./ul/li/a/@href').extract()
            for set_url in set_urls:
                yield scrapy.Request(set_url,callback=self.parse_detail)


    def parse_detail(self,response):
        for each in response.xpath('//body').xpath('./div[@class="content"]'):
            pic_urls = each.xpath('.//img/@src').extract()
            for pic_url in pic_urls:
                self.urllist.append(pic_url)

        if response.xpath('//div[@id="pages"]//a[last()]/text()').extract()[0] == "下一页":
            rel_url = response.xpath('//div[@id="pages"]//a[last()]/@href').extract()[0]
            next_url = urljoin('https://www.meitulu.com/',rel_url)
            yield scrapy.Request(next_url,callback=self.parse_detail)

        if response.xpath('//body').xpath('.//h1/text()').re(r'(.*?)\w+/\w+'):
            self.title = response.xpath('//body').xpath('.//h1/text()').re(r'(.*?)\w+/\w+')[0]
        return self.title, self.urllist

    def deal_item(self):
        item = MeituluItem()
        item['title'] = self.title
        item['url'] = self.urllist
        yield item
