import scrapy
from powerscrapy.items import PowerscrapyItem

class Ybyy_Spider(scrapy.Spider):
    name = "ybyy_spider"
    allowed_domains = ["yibuyy.com"]
    start_urls = ["http://www.yibuyy.com/frim/index1.html",
                  "http://www.yibuyy.com/frim/index2.html",
                  "http://www.yibuyy.com/frim/index42.html",
                  "http://www.yibuyy.com/frim/index44.html"]
    def parse(self, response):
        for sel in response.xpath('//*[@id="data_list"]/li[*]/div/a'):
            item = PowerscrapyItem()
            item['title'] = ''.join(sel.xpath('span[2]/text()').extract())
            item['url'] = "http://www.yibuyy.com"+''.join(sel.xpath('@href').extract())
            yield item
        next_page = response.xpath('//*[@class="page mb clearfixs"]/a[6]/@href').extract()
        if next_page is not None or next_page != []:
            yield scrapy.Request("http://www.yibuyy.com"+''.join(next_page),callback=self.parse)
