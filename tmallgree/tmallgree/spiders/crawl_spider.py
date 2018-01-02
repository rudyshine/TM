import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.selector import Selector
from tmallgree.items import TmallgreeItem

# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

class MySpider(CrawlSpider):
    name='gree'
    allowed_domains=['jd.com']
    start_url=["https://search.jd.com/search?keyword=%E6%A0%BC%E5%8A%9B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E6%A0%BC%E9%87%8C&stock=1&ev=exbrand_%E6%A0%BC%E5%8A%9B%EF%BC%88GREE%EF%BC%89%40424_78398%40&uc=0#J_searchWrap"]

    # rules=[]


    #获取链接
    def pare_item(self,response):
        item=[]
        print("===========")
        sel=Selector(response)
        link_url=sel.xpath('//*[@id="J_goodsList"]/ul/li/div/div/a/@href').extract()
        print(link_url)
        yield Request(url='https:'+link_url,callback=self.parse_dir_contents)

    #获取内容
    def parse_dir_contents(self,response):
        sel=Selector(response)
        item=TmallgreeItem()
        item['second_url']=response.url
        print(item['second_url'])
        item['title']=sel.xpath('/html/body/div/div/div/div/text()')
        print(item['title'])
        item['concent']=sel.xpath('//*[@id="comment-0"]/div/div/p/text()')
        print(item['concent'])
        yield  item