# -*- coding: utf-8 -*-
import scrapy
from MyScrapy.items import ImageaItem
from MyScrapy.webdrivers import Webdriver
from scrapy import Request
import mybasespider

class ImageSpider(mybasespider.WebdriverSpider):
    name = 'image'
    # allowed_domains = ['douyu.com']
    start_urls = ['http://www.budejie.com/pic', ]

    def parse(self, response):
        images = response.xpath('//img/@src')
        for img in images:
            item = ImageaItem()
            item['name'] = ""
            item['img_url'] = img.extract()

            if item['img_url'].startswith('http') and \
                    (item['img_url'].endswith('jpeg') or
                         item['img_url'].endswith('jpg') or
                         item['img_url'].endswith('gif') or
                         item['img_url'].endswith('png')):
                yield item
