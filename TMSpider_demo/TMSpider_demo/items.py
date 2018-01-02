# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmspiderDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #商品名称
    p_Name = scrapy.Field()
    #类别
    p_Type=scrapy.Field()
    #正价
    price = scrapy.Field()
    ##sellcount
    sellcount= scrapy.Field()
    ##ProductID
    ProductID = scrapy.Field()

    # p_link = scrapy.Field()
    pass
