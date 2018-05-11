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

    pagelink = LinkExtractor(restrict_xpaths='//div[@id="pages"]//a[last()]',allow=r'/\w+.html')
    rules = [
        Rule(pagelink, callback = "parse_picset_url", follow=True)
    ]



    def parse_picset_url(self, response):
        for each in response.xpath('//div[@class="boxs"]'):
            set_urls = each.xpath('./ul/li/a/@href').extract()
            for set_url in set_urls:
                yield scrapy.Request(set_url,callback=self.parse_pages)


    def parse_pages(self,response):
        try:
            item = MeituluItem()
            item['title'] = response.xpath('//h1/text()').extract_first()
            max_num = response.xpath('//div[@id="pages"]//a[last()-1]/text()').extract_first(default="N/A")
            tot_pic_num = response.xpath('//div[@class="c_l"]/p/text()').re(r'\d+\s+[\u5F20]')[0][:-1]
            base_pic_url = response.xpath('//div[@class="content"]/center/img/@src').extract_first()[:-5]
            pic_urls = [base_pic_url + '{}.jpg'.format(i) for i in range(1,int(tot_pic_num)+1) ]
            item['url'] = response.url
            item['image_urls'] = pic_urls
            yield item
        except Exception as e:
            print(e)


