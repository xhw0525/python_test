# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse

from MyScrapy.webdrivers import Webdriver
import time


class MyscrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# -------------------------------------------------------------------------------------------------------------------

# 下载中间件 //
class MyCustomDownloaderMiddleware(object):

    @classmethod
    def process_request(cls, request, spider): #此方法一直在单线程中调用
        if request.meta.get('webdriver'):
            Webdriver.get_instance().browser.get(request.url)
            content = Webdriver.get_instance().browser.page_source.encode('utf-8')
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        else:
            return None  # 返回 None, 交给下一个中间件  或者loader 处理

# -------------------------------------------------------------------------------------------------------------------

#斗鱼
class DouYUDownloaderMiddleware(object):

    @classmethod
    def process_request(cls, request, spider): #此方法一直在单线程中调用

        if request.meta.get('webdriver'):
            if request.meta.get('xiayiye'):
                view = Webdriver.get_instance().browser.find_element_by_xpath('//a[@class="shark-pager-next"]')
                if view:
                    view.click()
                else:
                    return
            else:
                Webdriver.get_instance().browser.get(request.url)
            js = "var q=document.getElementById('mainbody').scrollTop = 100000"
            Webdriver.get_instance().browser.execute_script(js)

            content = Webdriver.get_instance().browser.page_source.encode('utf-8')

            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        else:
            return None  # 返回 None, 交给下一个中间件  或者loader 处理


