# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from MyScrapy.webdrivers import Webdriver

class WebdriverSpider(scrapy.Spider):

    def start_requests(self):
        for url in self.start_urls:
            request = Request(url)
            request.meta['webdriver'] = True
            yield request

    @staticmethod
    def close(spider, reason):
        Webdriver.close()
        return scrapy.Spider.close(spider, reason)