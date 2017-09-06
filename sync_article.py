#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy
# Email: wxnacy@gmail.com
# Description:

from app.models import Article
from app.models import Category
from datetime import datetime

if __name__ == "__main__":
    begin = datetime.now().timestamp()
    Article.sync_data()
    #  Article.sync_timeline()
    end = datetime.now().timestamp()
    print('timed case: {}'.format(end-begin))
