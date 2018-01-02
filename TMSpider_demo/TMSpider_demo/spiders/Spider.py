# - * - coding: utf-8 - * -

from scrapy.spiders import CrawlSpider
from TMSpider_demo.items import TmspiderDemoItem
from scrapy.selector import Selector
from scrapy.http import Request
import re,time

class tmSpider(CrawlSpider):
    name = "Spider"
    redis_key = "Spider:start_urls"
    start_urls = [
        # 'https://list.tmall.com/search_product.htm?cat=50924011&brand=30652,30862,30645,21210,4536553,528788281' ##F (brand)
        #'https://list.tmall.com/search_product.htm?cat=56030006' ##y
        # 'https://list.tmall.com/search_product.htm?&cat=50924011&totalPage=11'1

        #'https://list.tmall.com/search_product.htm?&cat=50936008&totalPage=1'  62`
        'https://list.tmall.com/search_product.htm?cat=50924011'
    ]


    def parse(self, response):
        item = TmspiderDemoItem()
        selector = Selector(response)
        Products = selector.xpath('//*[@id="J_ItemList"]/div/div/div[3]/a[1]')
        print("len(Products):",len(Products))
        l=len(Products)
        for i in range(0,l):
            print(i)
            p_Name = selector.xpath('//*[@id="J_ItemList"]/div/div/div[3]/a[1]/text()').extract()[i]
            print("p_Name:",p_Name) 

            try:
                p_Type = selector.xpath('//*[@id="J_ItemList"]/div/div/div[3]/a[2]/text()').extract()[i]
            except IndexError:
                p_Type='none'

            price = selector.xpath('//*[@id="J_ItemList"]/div/div/p[1]/em/text()').extract()[i]
            print("price:", price)

            # sellcount= selector.xpath('//*[@id="J_ItemList"]/div/div/p[2]/span[1]/em/text()').extract()[i]
            # print("sellcount:", sellcount)//*[@id="J_ItemList"]/div[4]/div/p[2]/span[1]/em

            ID= selector.xpath('//div/@data-id').extract()[i]
            ProductID=int(ID)
            print("ProductID:", ProductID)

            # p_link=selector.xpath('//*[@id="J_ItemList"]/div/div/div[3]/a/@href')[i]

            item['p_Name'] = p_Name
            item['p_Type'] = p_Type
            print(item['p_Type'])
            item['price'] = price
            # item['sellcount'] = sellcount
            item['ProductID'] = ProductID
            # item['p_link']=p_link
            yield item

            donetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print("Sleep time start......")
            time.sleep(5)
            print("donetime is:", donetime)


        links = selector.xpath('//*[@class="ui-page-next"]/@href').extract()
        link =re.sub(r"['\?']", "", str(links))
        link=link[1:-1]
        print(link)
        if link:
            nextlink ='https://list.tmall.com/search_product.htm?'+link
            print("nextlink:",nextlink)
            time.sleep(10)
            yield Request(nextlink,callback=self.parse)