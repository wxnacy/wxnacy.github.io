#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from app.config import db
from app.models import VisitorLogDate
from app.models import VisitorLog
from app.models import Article
import time
from datetime import datetime
from datetime import date

if __name__ == "__main__":
    begin = time.time()

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
