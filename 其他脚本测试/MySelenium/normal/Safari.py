# -*- coding: utf-8 -*-
from selenium import webdriver
import json
import time
# browser = webdriver.PhantomJS('/Users/xhw/PythonV/phantomjs-2.1.1-macosx/bin/phantomjs')

browser = webdriver.Safari()

# browser.set_window_size(1000, 800)
# browser.set_page_load_timeout(10)  ##设置超时时间

browser.get("http://www.baidu.com")

cookies = browser.get_cookies()
with open('../../../result/haha.json', 'w+') as file :
    file.write(json.dumps(cookies,indent=1,sort_keys=True,separators=(',',':')))
# browser.delete_cookie('BD_UPN')

for cookie in cookies:
    if not cookie['name'].__contains__(u'BD_HOME'):
        print cookie['name']
        browser.delete_cookie(cookie['name'])
# browser.delete_all_cookies()
# browser.refresh()

print browser.get_cookies()


browser.close()
browser.quit()