#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from app.config import db
from app.models import VisitorLogDate
from app.models import VisitorLog
from app.models import Article
from app.models import ArticleData
import time
from datetime import datetime
from datetime import date
from flask_sqlalchemy import Pagination

if __name__ == "__main__":
    begin = time.time()

    #  ArticleData.statistics_article_data()
    #  Article.statistics_article()
    #  Article.get_crawler_data(url='https://wxnacy.com/2018/03/08/python-common-decorator')
    #  Article.crawler(url='https://wxnacy.com/2017/09/22/vim-plugin-tern/#libs')
    #  item = Article.query_by_id(68719477706)
    #  item.crawler_self()
    #  item.create_init_pv()
    #  Article.query.filter(Article.init_pv == 0)
    #  items = Article.query_items(init_pv = 0)
    #  print(len(items))
    #  for item in items:
        #  item.create_init_pv()

    #  Article.crawler_article()
    #  Article.statistics_init_pv()
    #  paginate = Article.query.filter_by().paginate(1, 3)
    #  print(paginate.has_next)
    #  print(paginate.has_prev)
    #  print(paginate.iter_pages())
    #  for i in paginate.iter_pages():
        #  print(i)
    #  print(paginate.next())
    #  print(paginate.next_num)
    #  print(paginate.pages)
    #  print(paginate.total)
    #  paginate = Pagination(Article.query.filter_by(), 1, 1, 1, None)
    #  print(paginate.items)

    #  vls = VisitorLog.query_items()
    #  for vl in vls:
        #  Article.crawler(url=vl.url)

    #  VisitorLogDate.statistics_visitor()

    vl = VisitorLog.query_item()
    Article.crawler(url=vl.url)
    now = date.today()
    year = now.year
    days = now.timetuple().tm_yday
    now_day = now.isoformat()
    print(now_day)
    article = Article.query_item(publish_date = now_day)
    print(f'{year} 年第 {days} 篇：{article.name} {article.url}')

    end = time.time()
    print('time :', (end-begin))
