# -*- coding: utf-8 -*-
import scrapy
import mybasespider

class BugtagsSpider(mybasespider.WebdriverSpider):
    name = 'bugtags'
    allowed_domains = ['bugtags']
    start_urls = ['http://bugtags/']

    def parse(self, response):
        pass
