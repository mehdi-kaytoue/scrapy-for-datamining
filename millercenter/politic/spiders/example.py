# -*- coding: utf-8 -*-
import scrapy
from politic.items import PoliticItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy import log


class ExampleSpider(CrawlSpider):
    name = "millercenter"
    allowed_domains = ["millercenter.org"]
    start_urls = (
        'http://millercenter.org/president/speeches/',
    )

    allow_rules = ['speeches/speech-', ]
    rules = [
        Rule(sle(allow=allow_rules), callback='parse_1', follow=True),
    ]


    def parse_1(self, response):
        item = PoliticItem()
        item['title'] = response.css('#amprestitle::text').extract()[0].split('(')[0][0:-1]
        item['date'] = response.css('#amprestitle::text').extract()[0].split('(')[1][0:-1]
        item['president'] = response.css('#innercontent > h2:nth-child(3)::text')[0].extract()
        item['text'] = response.css('#transcript > p:nth-child(1)::text').extract()
        item['url'] = response.url
        return item
