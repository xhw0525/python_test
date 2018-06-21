# -*- coding: utf-8 -*-
from selenium import webdriver

# 全局使用一个brower不知道会不会有问题? -------tmd
# 貌似scrapy 的 download 和 parse 都是是在单一线程完成的
# 那到底哪里是多线程并发啊啊啊?????exit
## 待优化

class Webdriver(object):

    __webdriver = None

    def __init__(self, show_img=True):
        self.browser = Webdriver.creat_browser_phantomjs(show_img)
        self.browser.set_window_size(800, 800)

        self.browser.implicitly_wait(15)  ##设置超时时间
        self.browser.set_page_load_timeout(15)  ##设置超时时间

    @staticmethod
    def get_instance(show_img=True):
        if Webdriver.__webdriver is None:
            Webdriver.__webdriver = Webdriver(show_img)
        return Webdriver.__webdriver

    @staticmethod
    def close():
        if Webdriver.__webdriver is not None:
            Webdriver.__webdriver.browser.quit()



    @staticmethod
    def creat_browser_firefox(show_img=True):
        option = webdriver.FirefoxOptions()
        # option.set_preference('permissions.default.image', 2) # 禁用图片
        option.add_argument(
            'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0')
        option.add_argument("-headless")
        browser = webdriver.Firefox(options=option)
        if not show_img:
            browser.set_preference('permissions.default.image', 2)
            # browser.set_preference('browser.migration.version', 9001)
        return browser

    @staticmethod
    def creat_browser_phantomjs(show_img=True):
        service_args = []
        if not show_img:
            service_args.append('--load-images=no')  ##关闭图片加载
        # service_args.append('--disk-cache=yes')  ##开启缓存
        service_args.append('--ignore-ssl-errors=true')  ##忽略https错误
        browser = webdriver.PhantomJS('/Users/xhw/PythonV/phantomjs-2.1.1-macosx/bin/phantomjs',
                                      service_args=service_args)
        return browser