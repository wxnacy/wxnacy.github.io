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
from sqlalchemy import desc
from flask import request
from datetime import datetime
import os
import re


FILE_LIST = os.listdir(BaseConfig.ARTICLE_DIR)
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


class Category(BaseModel,db.Model):
    __tablename__ = 'category'
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.String)
    content= db.Column(db.String,default="")
    ext = db.Column(db.JSON,default={})
    is_del = db.Column(db.INT,default=0)
    create_ts = db.Column(db.TIMESTAMP,default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP,default=datetime.now())

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

    @classmethod
    def sync_data(cls):
        cgs = cls.get_categorys()
        for cg in cgs:
            content = cls.get_md(cg,1)
            c = cls(name=cg,ext=dict(md=content))
            db.session.add(c)
        db.session.commit()


class Article(BaseModel,db.Model):
    __tablename__ = 'article'
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.String,default="")
    file_name = db.Column(db.String)
    publish_date = db.Column(db.DATE)
    category = db.Column(db.String,default="")
    content = db.Column(db.String,default="")
    ext = db.Column(db.JSON,default={})
    is_del = db.Column(db.INT,default=0)
    create_ts = db.Column(db.TIMESTAMP,default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP,default=datetime.now())

    @classmethod
    def sync_data(cls):
        file_list = os.listdir(BaseConfig.ARTICLE_DIR)
        file_list= list(filter(lambda x: not x.startswith('.'),file_list))

        Article.query.update(dict(is_del=1),synchronize_session=False)
        Category.query.update(dict(is_del=1),synchronize_session=False)
        cgs = {}
        def _save(o):
            md = Markdown(o)
            d = re.findall(RE_DATE,o)
            category = o.split('-')[0]
            a = cls(name=md.title,file_name=o,content=md.content,
                    publish_date=d,category=category)
            db.session.add(a)
            # category
            if category not in cgs:
                cgs[category] = []
            cgs[category].append('- [{}]({})'.format(md.title,md.route))

        [_save(o) for o in file_list]

        for k,v in cgs.items():
            content = '\n'.join(v)
            content = '# {}\n{}'.format(k,content)
            c = Category(name=k,content=content)
            db.session.add(c)

        db.session.commit()

        #  同步时间线数据
        #  content = cls.make_timeline()
        #  Config.sync(name='timeline',value=content)

    @classmethod
    def get_timeline_md(cls):
        item = Config.query_item(name='timeline')
        content = item.value if item else None
        return Markdown(content=content)


    @classmethod
    def make_timeline(cls):
        article = []
        items= {}
        for f in FILE_LIST:
            res = re.findall(RE_DATE,f)
            if res:
                if res[0] not in items:
                    items[res[0]] = []
                md = Markdown(f)
                items[res[0]].append('- [{}]({})'.format(md.title,md.route))

        items = [dict(d=k,items=v) for k,v in items.items()]
        items.sort(key=lambda x:x['d'],reverse=False)
        items.reverse()

        for i in items:
            article.append('## {}'.format(i['d']))
            for item in i['items']:
                article.append(item)

        content = '\n'.join(article)
        return  '# wxnacy 博客 \n[TOC]\n{}'.format(content)

    @classmethod
    def sync_timeline(cls):
        content = cls.make_timeline()
        Config.sync(name='timeline',value=content)

class Config(BaseModel,db.Model):
    id = db.Column(db.INT,primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.String,default='')
    ext = db.Column(db.JSON,default={})
    is_del = db.Column(db.INT,default=0)
    create_ts = db.Column(db.TIMESTAMP,default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP,default=datetime.now())

    @classmethod
    def sync(cls,**kwargs):
        name = kwargs.get('name')
        item = cls.query_item(name=name)
        if item:
            cls.update_by_id(id=item.id,**kwargs)
        else:
            cls.create(**kwargs)





if __name__ == "__main__":
    begin = datetime.now().timestamp()
    #  res = Article.get_timeline_md()
    #  print(res)
    Article.sync_data()
    #  Article.sync_timeline()
    #  res = Category.get_md('python',1)
    #  print(res)
    end = datetime.now().timestamp()
    print('timed case: {}'.format(end-begin))
