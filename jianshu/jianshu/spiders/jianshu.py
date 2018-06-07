#coding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from jianshu.items import JianshuItem

import urllib


class Jianshu(CrawlSpider):
    name = 'jianshu'   # 运行时这个爬虫的名字
    start_urls = ['http://www.jianshu.com']
    url = 'http://www.jianshu.com'

    def parse(self, response):
        item = JianshuItem()
        selector = Selector(response)
        print(selector)
        #....
        # response就是返回的网页数据
        # 处理好的数据放在items中，在items.py设置好你要处理哪些数据字段，这里我们抓取文章标题，url，作者，阅读数，喜欢，打赏数
        ## 解析处理数据的地方，用xpath解析处理数据

