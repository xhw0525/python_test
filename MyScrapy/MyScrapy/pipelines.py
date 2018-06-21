# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request
from MyScrapy.items import ImageaItem
import sqlite3
import os
import MyScrapy.settings as Settings

reload(sys)
sys.setdefaultencoding('utf8')

class MyscrapyFilePipeline(object):
    def __init__(self):
        self.f = open(os.getcwd() + "/result/" + self.__class__.__name__ + ".txt", "w+")

    def process_item(self, item, spider):
        if spider.name == 'haha':
            self.f.write(item["a"] + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()



class MyscrapyDBPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(Settings.BASE_DIR, 'result/db.sqlite3'))

    def process_item(self, item, spider):
        if spider.name == 'haha':
            cursor = self.conn.cursor()
            sqlstr = """insert into biaoqian (name, a) VALUES (?, ?)"""
            # param = (unicode(item['name']), unicode(item['a']))
            param = (item['name'], item['a'])
            cursor.execute(sqlstr, param)
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.conn.close()

#//ImagesPipeline 自动下载
class MyFilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        if type(item) == ImageaItem and item['img_url'] is not None:
            yield Request(item['img_url'])
        else:
            yield None

    def item_completed(self, results, item, info):
        for ok, x in results:
            if ok and len(item['name']) and os.path.exists(Settings.FILES_STORE + x['path']):
                oldpath = Settings.FILES_STORE + x['path']
                newpath = Settings.FILES_STORE + item['name'] + os.path.splitext(x['path'])[1]
                os.rename(oldpath, newpath)
            else:
                print ('下载失败')
        return item
