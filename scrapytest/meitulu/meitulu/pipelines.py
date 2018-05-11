# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline



class MeituluPipeline(ImagesPipeline):

    def file_path(self,request,response=None,info=None):
        item = request.meta['item']
        folder = item['title']
        folder = strip(folder)
        file_path = '/{}/'.format(folder)
        return file_path

    def get_media_requests(self, item, info):
        for img_url in item['image_urls']:
            referer = item['url']
            yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item



def strip(path):
    """
    :param path: 需要清洗的文件夹名字
    :return: 清洗掉Windows系统非法文件夹名字的字符串
    """
    path = re.sub(r'[？\\*|“<>:/]', '', str(path))
    return path
