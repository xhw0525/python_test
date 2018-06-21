# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from MyScrapy.webdrivers import Webdriver
from MyScrapy.items import MyscrapyItem
import mybasespider

class HahaSpider(mybasespider.WebdriverSpider):

    name = 'haha'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com']

    def parse(self, response):

        lista = response.xpath("//a")
        for alink in lista:
            item = MyscrapyItem()
            item['a'] = alink.xpath('@href').extract()[0]
            if alink.xpath('text()'):
                item['name'] = alink.xpath('text()').extract()[0]
            else:
                item['name'] = unicode('未获取到')

            yield item
            # yield Request("http://hahahahfah.com", callback=self.parse)
