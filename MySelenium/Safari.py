# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

service_args = []
desire = DesiredCapabilities.PHANTOMJS.copy()
headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive',
           }
for key, value in headers.iteritems():
    desire['phantomjs.page.customHeaders.{}'.format(key)] = value
service_args.append('--ignore-ssl-errors=true')     # 忽略https错误
browser = webdriver.PhantomJS('/Users/xhw/PythonV/phantomjs-2.1.1-macosx/bin/phantomjs',desired_capabilities=desire,
                                  service_args=service_args)

# browser = webdriver.Safari() #如出错 请下载最新selenium

# browser.set_window_size(1000, 800)
# browser.set_page_load_timeout(10)  ##设置超时时间

browser.get("https://www.niaogebiji.com/wap/mims/votedetail/?id=340&from=groupmessage&isappinstalled=0")
# cookies = browser.get_cookies()
# with open('result/haha.json', 'w+') as file :
#     file.write(json.dumps(cookies,indent=2,sort_keys=True,separators=(',',':')))
# # browser.delete_cookie('BD_UPN')
#
# for cookie in cookies:
#     if not cookie['name'].__contains__(u'BD_HOME'):
#         print cookie['name']
#         browser.delete_cookie(cookie['name'])
# # browser.delete_all_cookies()
# # browser.refresh()
#
# print browser.get_cookies()
#
#
# browser.close()
# browser.quit()
time.sleep(5)

closebtn = browser.find_element_by_xpath('//*[@id="votedetail"]/div[3]/div[1]')
time.sleep(1)

ActionChains(browser).click(closebtn).perform()
time.sleep(0.5)
ActionChains(browser).click(closebtn).perform()

# browser.execute_script('_czc.push(["_trackEvent","金名奖详情页面","投票","点击按钮", 0,"vote"]);');

browser.save_screenshot('haha.png')
browser.quit()

