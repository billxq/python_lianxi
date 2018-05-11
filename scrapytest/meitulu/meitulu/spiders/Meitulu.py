# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meitulu.items import MeituluItem


class MeituluSpider(CrawlSpider):
    title = ''
    img_urls = list()
    name = 'Meitulu'
    allowed_domains = ['www.meitulu.com']
    start_urls = ['https://www.meitulu.com/t/toutiaonvshen/']

    pagelink = LinkExtractor(restrict_xpaths='//div[@id="pages"]//a[last()]',allow=r'/\w+.html',deny=r'/\w+_\w+.html')
    rules = [
        Rule(pagelink, callback = "parse_picset_url", follow=True)
    ]


    def parse_picset_url(self, response):
        for each in response.xpath('//div[@class="boxs"]'):
            set_urls = each.xpath('./ul/li/a/@href').extract()
            for set_url in set_urls:
                yield scrapy.Request(set_url,callback=self.parse_item)


    def parse_item(self,response):
        item = MeituluItem()
        item['title'] = response.xpath('//title/text()').extract_first(default="N/A")
        item['url'] = response.url

        if response.xpath('//div[@id="pages"]//a[last()-1]/text()'):
            max_num = response.xpath('//div[@id="pages"]//a[last()-1]/text()').extract_first(default="N/A")

        page_urls = [ response.url[:-5] + '_{}.html'.format(i) for i in range(2,int(max_num)+1)]
        for page_url in page_urls:
            yield scrapy.Request(page_url,callback=self.img_url)
        item['image_urls'] = self.img_urls
        yield item

    def img_url(self,response):
        img_urls = response.xpath('//div[@class="content"]//img/@src').extract()
        for img_url in img_urls:
            self.img_urls.append(img_url)






