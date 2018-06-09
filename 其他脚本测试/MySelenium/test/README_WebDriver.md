
// 哈哈 浏览器也可以 无界面
option = webdriver.FirefoxOptions()
option.add_argument("--headless")

//滑到底部
js="var q=document.documentElement.scrollTop += document.body.scrollHeight"
//或者
js="var q=document.getElementById('节点id').scrollTop += document.getElementById('节点id').scrollHeight"

browser.execute_script(js)

# 全局使用一个brower不知道会不会有问题?
# option = webdriver.FirefoxOptions()
# option.add_argument("-headless")
# browser = webdriver.Firefox(options=option)
# browser.set_window_size(1200, 800)
# browser.implicitly_wait(5)  ##设置超时时间
# browser.set_page_load_timeout(5)  ##设置超时时间



# browser.get('about:blank')  # 爬坑: PhantomJS重用时, 一次请求完 重置状态
# browser.close(); <or> browser.quit();
#


selenium firefox46.0.1设置禁用图片
 firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)#某些firefox只需要这个
firefox_profile.set_preference('browser.migration.version', 9001)#部分需要加上这个
禁用css
firefox_profile.set_preference('permissions.default.stylesheet', 2)
禁用flash
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
禁用js
firefox_profile.set_preference('javascript.enabled', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://re.jd.com/'）



#######################3/////关于代理

# 不使用代理代打开ip138
browser=webdriver.PhantomJS(PATH_PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')
print('1: ',browser.session_id)
print('2: ',browser.page_source)
print('3: ',browser.get_cookies())

# 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy='1.9.171.51:800'
# 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')
print('1: ',browser.session_id)
print('2: ',browser.page_source)
print('3: ',browser.get_cookies())

# 还原为系统代理
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.DIRECT
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')



#bugtags 模拟登陆
# browser.get("https://work.bugtags.com/login.html")
#
# user = browser.find_element_by_id('login_email')
# user.send_keys('1982700252@qq.com')
# pwd = browser.find_element_by_id('login_pwd')
# pwd.send_keys('Zx.666555')
# time.sleep(1)
#
# browser.find_element_by_id('btn_login').click()
#
# browser.find_element_by_id('btn_login').click()
#
# time.sleep(10)
#
#