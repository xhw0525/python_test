# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from MyScrapy.webdrivers import Webdriver
from MyScrapy.items import ImageaItem
import mybasespider
import hashlib
class DouyuSpider(mybasespider.WebdriverSpider):
    name = 'douyu'
    # allowed_domains = ['douyu.cn']
    start_urls = ['https://www.douyu.com/directory/game/yz']

    count = 0
    def parse(self, response):
        imgs_parents = response.xpath('//body/div[1]/div[3]/div[1]/div/div/div[3]/ul/li')
        for imgs_parent in imgs_parents:
            imgs = imgs_parent.xpath('a')
            if len(imgs) > 0:
                item = ImageaItem()
                item['name'] = imgs[0].xpath('div/p/span[1]/text()').extract()[0]

                item['img_url'] = imgs[0].xpath('span/img/@data-original').extract()[0]
                yield item

        imgs_parents2 = response.xpath('//body/div[2]/div[3]/div[1]/div/div/div[3]/ul/li')
        for imgs_parent in imgs_parents2:
            imgs = imgs_parent.xpath('a')
            if len(imgs) > 0:
                item = ImageaItem()
                item['name'] = imgs[0].xpath('div/p/span[1]/text()').extract()[0]

                item['img_url'] = imgs[0].xpath('span/img/@data-original').extract()[0]

                yield item

        self.count += 1
        if  self.count == 16:
            return
        request = Request('https://www.douyu.com/directory/game/yz'+ str(self.count), dont_filter=True)
        request.meta['webdriver'] = True
        request.meta['xiayiye'] = True
        yield request

