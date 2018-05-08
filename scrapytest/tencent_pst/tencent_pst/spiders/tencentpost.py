# -*- coding: utf-8 -*-
import scrapy
from urllib.request import urljoin
from tencent_pst.items import TencentPstItem

class TencentpostSpider(scrapy.Spider):
    name = 'tencentpost'
    allowed_domains = ['tencent.com']
    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(offset)]

    def parse(self, response):
        try:
            xpattern = response.xpath('//tr[(@class="odd" or @class="even")]')
            for card in xpattern:
                item = TencentPstItem()
                post = card.xpath('.//a/text()').extract()[0]
                post_url = card.xpath('.//a/@href').extract()[0]
                job_type = card.xpath('./td[2]/text()').extract()[0]
                ppl_recru = card.xpath('./td[3]/text()').extract()[0]
                place = card.xpath('./td[4]/text()').extract()[0]
                post_date = card.xpath('./td[last()]/text()').extract()[0]
                item['post'] = post
                item['post_url'] = urljoin(response.url,post_url)
                item['job_type'] = job_type
                item['ppl_recru'] = ppl_recru
                item['place'] = place
                item['post_date'] = post_date
                yield item
        except:
            pass
        if self.offset <= 3850:
            self.offset += 10
        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)

