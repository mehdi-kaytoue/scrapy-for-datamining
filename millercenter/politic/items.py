# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoliticItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    president = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()
    pass
