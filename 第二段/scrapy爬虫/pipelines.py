# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['image_urls']
        yield scrapy.Request(image_url,meta={'name':item['image_name']})
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
    def file_path(self, request, response=None, info=None):
        name = request.meta['name']    # 接收上面meta传递过来的图片名称                                        
        filename= name +'.jpg'          #添加图片后缀名
        return filename
