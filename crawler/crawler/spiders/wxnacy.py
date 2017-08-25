#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''wxnacy spider'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."
from crawler.crawler.items import WxnacyItem
import scrapy



class WxnacySpider(scrapy.Spider):
    name = "wxnacy"
    allowed_domains = ["wxnacy.com"]
    start_urls = ['http://wxnacy.com/']

    def parse(self, response):
        wi = WxnacyItem()
        wi['title'] = response.css('title::text').extract_first()
        print(wi)
        yield wi
