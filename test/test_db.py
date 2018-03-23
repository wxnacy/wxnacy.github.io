#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from app.config import db
from app.models import VisitorLogDate
from app.models import VisitorLog
from app.models import Article
import time

if __name__ == "__main__":
    begin = time.time()
    vls = VisitorLog.query_items()
    for vl in vls:
        Article.crawler(url=vl.url)
    end = time.time()
    print('time :', (end-begin))
