#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.models import VisitorLogDate
from app.models import Article
from app.models import ArticleData
from app.config import app
from flask_apscheduler import APScheduler

scheduler = APScheduler(app=app)
scheduler.add_job('statistics_visitor', VisitorLogDate.statistics_visitor,
                  trigger='interval', seconds=100)
scheduler.add_job('statistics_article_data', ArticleData.statistics_article_data,
                  trigger='interval', seconds=66)
scheduler.add_job('statistics_pv', Article.statistics_pv,
                  trigger='interval', seconds=360)
scheduler.add_job('statistics_article', Article.statistics_article,
                  trigger='interval', seconds=350)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True, port=8003)
