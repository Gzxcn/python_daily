#coding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from ithome.items import IthomeItem

import urllib


class Ithome(CrawlSpider):
    name = 'ithome'   # 运行时这个爬虫的名字
    start_urls = ['https://www.ithome.com/']
    url = 'https://www.ithome.com/'
    next_url = []
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Host': 'www.baidu.com',
    #     'Cache-Control': "max-age=0",
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
    #     "Upgrade-Insecure-Requests": 1,
    #     "Cookie": "BIDUPSID=5B08D3236FB056B4E5D5FA09BE167913; PSTM=1519971608; __cfduid=d91fa98c5ef17922d268e572efc33b6781521188548; BAIDUID=C45F61E092F1949C359FE55B1AFA7647:FG=1; ISSW=1; BD_UPN=12314753; locale=zh; BDUSS=y1RenRtZ0dSTmxlZEN3NUtwb0xDR3FkNUR4LVE4SElhcFUxOEF0aHYyY05WRFJiQVFBQUFBJCQAAAAAAAAAAAEAAAA-BqlEsvHD19PN0c6017Lo2LwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3HDFsNxwxbV; pgv_pvi=3084246016; cflag=15%3A3; BD_HOME=1; H_PS_PSSID=1457_21084_18559_26432_26580_22157; pgv_si=s3103722496"
    # }
    # cookies = {
    #     "BAIDUID": "C45F61E092F1949C359FE55B1AFA7647:FG=1",
    #     "BDUSS": "y1RenRtZ0dSTmxlZEN3NUtwb0xDR3FkNUR4LVE4SElhcFUxOEF0aHYyY05WRFJiQVFBQUFBJCQAAAAAAAAAAAEAAAA-BqlEsvHD19PN0c6017Lo2LwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3HDFsNxwxbV",
    #     "BD_HOME" : "1",
    #     "BD_UPN": "12314753",
    #     "BIDUPSID": "5B08D3236FB056B4E5D5FA09BE167913",
    #     "H_PS_PSSID" : "1457_21084_18559_26432_26580_22157",
    #     "ISSW" : "1",
    #     "PSTM": "1519971608",
    #     "__cfduid": "d91fa98c5ef17922d268e572efc33b6781521188548",
    #     "cflag": "15%3A3",
    #     "locale": "zh",
    #     "pgv_pvi": "3084246016",
    #     "pgv_si": "s3103722496"
    # } 
    def parse(self, response) :
        item = IthomeItem()
        selector = Selector(response)

        articles = selector.xpath("//div[@class='block 8250 new-list-1']/ul")
        # print(articles)
        j = 0
        for article in articles :
            # title = article.xpath("//li/span[2]/a/text()").extract()
            href = article.xpath("//li/span[2]/a/@href").extract()
            # time = article.xpath("//li/span[@class='date']/text()").extract()

            # item["title"] = title 
            # item["href"] = href
            # item["time"] = time
            real_link = href 
            if(real_link) :   
                # print(real_link)  
                if j == 0 :
                    for i in real_link : 
                        # print(i)
                        j = 1
                        yield Request(i, callback=self.real_parse)
               
            # print(time)
        # ....
        # response就是返回的网页数据
        # 处理好的数据放在items中，在items.py设置好你要处理哪些数据字段，这里我们抓取文章标题，url，作者，阅读数，喜欢，打赏数
        ## 解析处理数据的地方，用xpath解析处理数据

    def real_parse(self, response) :
        
        item = IthomeItem()
        selector = Selector(response)
        # article = selector.xpath("//div[@class='content fl']").extract()
        article = selector.xpath("//div[@class='content fl']/div[1]")
        title = article.xpath("//h1/text()").extract()
        details = selector.xpath("//div[@id='paragraph']//p").extract()
      
        item['title'] = title
        item["detail"] = details
        yield item
        

