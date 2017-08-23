#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''pipeline'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from app.models import Crawler


class CrawlerPipeline(object):
    def open_spider(self, spider):
        spider.logger.debug('{} open'.format(spider.name))

    def close_spider(self, spider):
        spider.logger.debug('{} close'.format(spider.name))

    def process_item(self, item, spider):
        print('pipe %s' % item)

        Crawler.create(url=spider.start_urls[0], ext=dict(item))
        return item
