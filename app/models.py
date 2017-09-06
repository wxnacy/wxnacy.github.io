#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''models'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseModel
from app.common.md import Markdown
from app.common.security import Md5
from app.config import db
from app.config import BaseConfig
from datetime import datetime
from sqlalchemy.orm import backref as b
from flask import request
import os
import re


FILE_LIST = os.listdir(BaseConfig.ARTICLE_DIR)
FILE_LIST.reverse()
FILE_LIST = list(filter(lambda x: not x.startswith('.'),FILE_LIST))

RE_DATE = re.compile(u"\d{4}-\d{2}-\d{2}")  # 正则时间类型


class Crawler(BaseModel, db.Model):
    __tablename__ = 'crawler'
    id = db.Column(db.INT, primary_key=True)
    url = db.Column(db.String)
    ext = db.Column(db.JSON, default={})
    is_del = db.Column(db.INT, default=0)
    create_ts = db.Column(db.TIMESTAMP, default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP, default=datetime.now())


class VisitUser(BaseModel, db.Model):
    __tablename__ = 'visit_user'
    id = db.Column(db.INT, primary_key=True)
    ip = db.Column(db.String)
    user_agent = db.Column(db.String, default="")
    md5 = db.Column(db.String, default="")
    ext = db.Column(db.JSON, default={})
    is_del = db.Column(db.INT, default=0)
    create_ts = db.Column(db.TIMESTAMP, default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP, default=datetime.now())

    @classmethod
    def generate_md5(cls, ip, user_agent):
        return Md5.encrypt('{};{}'.format(ip, user_agent))

    @classmethod
    def log(cls):
        headers = request.headers
        ip = request.remote_addr
        user_agent = request.user_agent

        md5 = cls.generate_md5(ip, user_agent)
        user = cls.query_item(md5=md5)
        if not user:
            user = cls(ip=ip, user_agent=str(user_agent), md5=md5,
                              ext=dict(headers))
            user.create_self()
        return user.visit()

    def visit(self):
        return VisitLog.create(visit_user_id=self.id, url=request.url,
                               method=request.method,
                               referrer=request.referrer,
                               ext=dict(request.headers))


class VisitLog(BaseModel, db.Model):
    __tablename__ = 'visit_log'
    id = db.Column(db.INT, primary_key=True)
    visit_user_id = db.Column(db.INT, db.ForeignKey('visit_user.id'))
    method = db.Column(db.String, default="")
    url = db.Column(db.String, default="")
    referrer = db.Column(db.String, default="")
    ext = db.Column(db.JSON, default={})
    is_del = db.Column(db.INT, default=0)
    create_ts = db.Column(db.TIMESTAMP, default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP, default=datetime.now())

    visit_user = db.relationship('VisitUser',
                                 backref=b('visit_logs', lazy='dynamic'))


class Category():

    @classmethod
    def get_categorys_md(cls):
        article = [ '# 分类' ]
        for cg in cls.get_categorys():
            article.append('- [{}](/{})'.format(cg,cg))
        content = '\n'.join(article)
        return Markdown(content=content)

    @classmethod
    def get_categorys(cls):
        categorys = list(set([o.split('-', 1)[0] for o in FILE_LIST]))
        #  categorys = list(filter(lambda x: x in CATEGORYS, categorys))
        FILTER=['.DS_Store']
        categorys = list(filter(lambda x: not x.startswith('.') , categorys))
        categorys.sort()
        return categorys

    @classmethod
    def get_md(cls,category, level):
        """生成分类文章md内容"""
        file_list = list(filter(lambda x: 'item' not in x, FILE_LIST))
        file_list.sort()
        article = []
        article.append('{} {}'.format('#' * level, category))
        items = []
        for file in file_list:
            mf = Markdown(file)
            profix = '专辑' if 'album' in mf.route else '文章'
            res = re.findall(RE_DATE, mf.route)
            date = ''
            if res:
                date = res[0]
            items.append(
                '- {} [{}] [{}]({})'.format(date, profix, mf.title, mf.route))
            items.sort(reverse=True)
        article.extend(items)

        return '\n'.join(article)


class Article():

    @classmethod
    def get_timeline_md(cls):
        article = ['# wxnacy 博客\n']
        for f in FILE_LIST:
            res = re.findall(RE_DATE,f)
            if res:
                md = Markdown(f)
                article.append('- [{}] [{}]({})'.format(res[0],md.title,md.route))
        content = '\n'.join(article)
        return Markdown(content=content)

if __name__ == "__main__":
    res = Article.get_timeline_md()
    #  print(res)
