source ~/PythonU/bin/activate  进入python虚拟环境
source ~/PythonU/bin/activate; cd ~/PycharmProjects/MyScrapy;

#   scrapy startproject project_name
#   scrapy genspider [-t template] <name> <domain>

#   scrapy genspider haha www.baidu.com
scrapy genspider OneSpider "www.baidu.com"

crawl
scrapy crawl <spider>
使用spider进行抓取
scrapy crawl weather

check
scrapy check [-l] <spider>
运行contract检查

list
scrapy list
列出当前项目中所有可用的spider，每一行输出一个spider。
