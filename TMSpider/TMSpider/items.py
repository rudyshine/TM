# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmspiderItem(scrapy.Item):
    # define the fields for your item here like:
    productPrice = scrapy.Field()
    productStatus = scrapy.Field()
    productType = scrapy.Field()
    productName = scrapy.Field()
    pass
