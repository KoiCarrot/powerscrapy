# -*- coding : utf-8 -*-
import scrapy
from powerscrapy.items import PowerscrapyItem
class hanjuTV_spider(scrapy.Spider):
    name = 'hanjuTV_spider'
    allowed_domains = ['hanju.cc']
    start_urls = ['http://www.hanju.cc/hanju/']
    def parse(self, response):
        for sel in response.xpath('//*[@class="stab-con"]/dl/dd/li'):
            item = PowerscrapyItem()
            item['title'] = '韩剧TV-'+''.join(sel.xpath('div[1]/span/a/b/text()').extract())
            item['url'] = 'http://www.hanju.cc'+''.join(sel.xpath('a/@href').extract())
            yield item
        # next_page = response.xpath('//*[@id="sdlist"]/div[2]/div[1]/div[2]/li[13]/a/@href').extract()
        # if next_page is not None or next_page != []:
        for i in range(1,68):
            yield scrapy.Request('http://www.hanju.cc/hanju/list_8_'+str(i)+'.html', callback=self.parse)