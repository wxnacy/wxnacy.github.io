#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.crawler.spiders.wxnacy import WxnacySpider

process = CrawlerProcess(get_project_settings())
process.crawl(WxnacySpider)
process.start()
