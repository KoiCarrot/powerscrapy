# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class PowerscrapyPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            db = 'powerscrapy',
            user = 'root',
            passwd = 'SmileGirl@123',
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        self.cursor.execute('insert into Yibuyy(title,url)values(%s,%s)',(item['title'],item['url']))
        self.connect.commit()
        return item
