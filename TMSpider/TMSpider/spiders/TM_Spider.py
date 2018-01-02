# - * - coding: utf-8 - * -
from scrapy.spiders import CrawlSpider
from TMSpider.items import TmspiderItem
from scrapy.selector import Selector
from scrapy.http import Request
from bs4 import BeautifulSoup
import time
import requests
import re, json



class TmSpider(CrawlSpider):
    name = "TmSpider"
    redis_key = "JDSpider:start_urls"
    start_urls = [
                "https://list.suning.com/0-20368-0-0-0-0-0-0-0-0-10018a45472a10017a10069a10132a56664.html"
        ]
    # print("111111111111111")
    def parse(self, response):
        # print("111111111111111")
        item = TmspiderItem()
        selector = Selector(response)
        Products = selector.xpath('//*[@id="filter-results"]/ul/li')
        for each in Products:
            productPrice =each.xpath('//div/div/div/div[2]/p[1]/em/text()/text()').extract()
            # print("111111111111111",productPrice)
            productStatus =each.xpath('//div/div/div/div[2]/p[3]/a[1]/text()').extract()
            print(productStatus)
            # productType = each.xpath('//*[@id="J_ItemList"]/div[1]/div/div[3]/a[2]/text()').extract()
            # print(productType)
            productName =each.xpath('//div/div/div/div[2]/p[2]/a/em/text()').extract()
            print(productName)

        item['productPrice'] = productPrice
        item['productStatus']= productStatus
        # item['productType'] = productType
        item['productName'] = productName
        yield item

        # nextLink = selector.xpath('//*[@id="nextPage"]').extract()
        # print("nextLink:",nextLink)
        # if nextLink:
        #     nextLink = nextLink[0]
        #     yield Request('https://list.suning.com/'+nextLink,callback=self.parse)

