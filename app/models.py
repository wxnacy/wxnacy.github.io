#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''models'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseModel as BM
from app.common.base import BaseDB
from app.common.md import Markdown
from app.common.security import Md5
from app.config import db
from app.config import BaseConfig
from app.config import logger
from datetime import datetime
from datetime import date
from sqlalchemy.orm import backref as b
from sqlalchemy import desc
from sqlalchemy import or_
from sqlalchemy import text
from sqlalchemy import func
from flask import request
from user_agents import parse
import os
import re
import time


FILE_LIST = os.listdir(BaseConfig.ARTICLE_DIR)
FILE_LIST = list(filter(lambda x: not x.startswith('.'),FILE_LIST))

RE_DATE = re.compile(u"\d{4}-\d{2}-\d{2}")  # 正则时间类型

class BaseModel(BM):

    @classmethod
    def create(cls, **params):
        params['id'] = AutoId.generate_id()
        item = super().create(**params)
        return item


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
                               method=request.method,path=request.path,
                               referrer=request.referrer,
                               domain=request.headers.get('host'),
                               ext=dict(request.headers))


class VisitLog(BaseModel, db.Model):
    __tablename__ = 'visit_log'
    id = db.Column(db.INT, primary_key=True)
    visit_user_id = db.Column(db.INT, db.ForeignKey('visit_user.id'))
    method = db.Column(db.String, default="")
    domain = db.Column(db.String,default="")
    url = db.Column(db.String, default="")
    path = db.Column(db.String, default="")
    referrer = db.Column(db.String, default="")
    ext = db.Column(db.JSON, default={})
    is_del = db.Column(db.INT, default=0)
    create_ts = db.Column(db.TIMESTAMP, default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP, default=datetime.now())

    visit_user = db.relationship('VisitUser',
                                 backref=b('visit_logs', lazy='dynamic'))

    @classmethod
    def get_count_by_url(cls,url):
        return cls.query.filter(cls.url.like('%{}'.format(url))
                ).count()


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
    view_count = db.Column(db.INT,default=0,doc="观看数量")
    route = db.Column(db.String,default="")
    content = db.Column(db.String,default="")
    ext = db.Column(db.JSON,default={})
    is_del = db.Column(db.INT,default=0)
    create_ts = db.Column(db.TIMESTAMP,default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP,default=datetime.now())

    @classmethod
    def search(cls,q):
        s = '%{}%'.format(q)
        items = Article.query.filter(or_(
                Article.name.like(s),Article.content.like(s)
            ),Article.is_del==0).order_by(desc(Article.publish_date)).all()

        md = []
        for i in items:
            md.append('- [{}]({})'.format(i.name,i.route))

        content = '# 搜素：{}\n{}'.format(q,'\n'.join(md))
        return Markdown(content=content)


    @classmethod
    def sync_data(cls):
        file_list = os.listdir(BaseConfig.ARTICLE_DIR)
        file_list= list(filter(lambda x: not x.startswith('.'),file_list))

        Article.query.update(dict(is_del=1),synchronize_session=False)
        Category.query.update(dict(is_del=1),synchronize_session=False)
        cgs = {}
        timeline = {}
        def _save(o):
            md = Markdown(o)
            d = re.findall(RE_DATE,o)[0]
            category = o.split('-')[0]
            vc = VisitLog.get_count_by_url(md.route)
            a = cls(name=md.title,file_name=o,content=md.content,
                    publish_date=d,category=category,route=md.route,
                    view_count=vc)
            db.session.add(a)
            # category
            if category not in cgs:
                cgs[category] = []
            cgs[category].append('- [{}]({})'.format(md.title,md.route))
            # timeline
            if d not in timeline:
                timeline[d] = []
            timeline[d].append('- [{}]({})'.format(md.title,md.route))

        [_save(o) for o in file_list]

        # 将category format并放入到session中
        for k,v in cgs.items():
            content = '\n'.join(v)
            content = '# {}\n{}'.format(k,content)
            c = Category(name=k,content=content)
            db.session.add(c)

        # format and save timeline
        timeline = [dict(d=k,items=v) for k,v in timeline.items()]
        timeline.sort(key=lambda x:x['d'],reverse=False)
        timeline.reverse()

        tl = []
        for i in timeline:
            tl.append('## {}'.format(i['d']))
            for item in i['items']:
                tl.append(item)

        tl = '\n'.join(tl)
        tl = '# wxnacy 博客 \n[TOC]\n{}'.format(tl)
        Config.sync(name='timeline',value=tl)

        db.session.commit()


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

    @classmethod
    def count(cls):
        return cls.query.filter(
                cls.is_del == 0
                ).count()

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


class Code(BaseModel,db.Model):
    __tablename__ = 'code'
    id = db.Column(db.String,primary_key=True)
    name = db.Column(db.String,default="")
    description = db.Column(db.String,default="")
    type = db.Column(db.String,default="")
    code = db.Column(db.JSON,default={})
    is_available = db.Column(db.INT,default=1)
    create_ts = db.Column(db.TIMESTAMP,default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP,default=datetime.now())

class AutoId(BaseModel, db.Model):
    __tablename__ = 'auto_id'
    id = db.Column(db.INT,primary_key=True)
    shard_id = db.Column(db.INT, default = 0)
    item_id = db.Column(db.INT, default = 1)

    @classmethod
    def generate_id(cls, shard_id = 0, item_id = 1):
        sql = 'select func_auto_id(%s, %s) as id'
        res = BaseDB.query(sql, [shard_id, item_id])
        return res[0]['id']

class User(BaseModel, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String, default = '')
    email = db.Column(db.String, default = '')
    mobile = db.Column(db.String, default = '')
    password = db.Column(db.String, default = '')
    status = db.Column(db.String, default = '')
    type = db.Column(db.String, default = '')
    ext_property = db.Column(db.JSON, default={})
    is_available = db.Column(db.INT, default=1)
    create_ts = db.Column(db.TIMESTAMP, default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP, default=datetime.now())

class VisitorLog(BaseModel, db.Model):
    __tablename__ = 'visitor_log'
    id = db.Column(db.INT, primary_key=True)
    ip = db.Column(db.String, default = '')
    url = db.Column(db.String, default = '')
    referrer = db.Column(db.String, default = '')
    user_agent = db.Column(db.String, default = '')
    os = db.Column(db.String, default = '')
    device = db.Column(db.String, default = '')
    device_type = db.Column(db.String, default = '')
    browser = db.Column(db.String, default = '')
    md5 = db.Column(db.String, default = '')
    visit_date = db.Column(db.Date, default = date.today)
    is_bot = db.Column(db.INT, default=0)
    ext_property = db.Column(db.JSON, default={})
    is_available = db.Column(db.INT, default=1)
    create_ts = db.Column(db.TIMESTAMP, default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP, default=datetime.now())

    @property
    def region(self):
        ext = self.ext_property
        return '{}-{}'.format(ext.get('country_name'), ext.get('city'))

    @classmethod
    def query_items(cls, **kw):
        query_date = kw.get('date', date.today().isoformat())
        logger.debug(query_date)
        sql = 'is_bot = 0 and is_available = 1 and url like "%wxnacy.com%"\
                and visit_date = :date'
        items = cls.query.filter(text(sql)).params(
            date = query_date
        ).order_by(desc(cls.create_ts)).all()
        return items

    @classmethod
    def visit(cls, **kw):
        begin = time.time()
        ua = kw['user_agent']
        ua = parse(ua)
        kw['os'] = ua.os.family
        kw['device'] = ua.device.family
        kw['browser'] = ua.browser.family
        device_type = 'pc'
        if ua.is_mobile:
            device_type = 'mobile'
        elif ua.is_tablet:
            device_type = 'tablet'
        kw['device_type'] = device_type
        kw['is_bot'] = ua.is_bot
        kw['md5'] = Md5.encrypt('{};{}'.format(kw['ip'], kw['user_agent']))
        kw['visit_date'] = date.today()

        res = VisitorLog.create(**kw)
        end = time.time()
        logger.debug('visit time: %s', (end-begin))
        return res

class VisitorLogDate(BaseModel, db.Model):
    __tablename__ = 'visitor_log_date'
    id = db.Column(db.INT, primary_key=True)
    visit_date = db.Column(db.Date, default = date.today)
    pv = db.Column(db.INT, default=0)
    uv = db.Column(db.INT, default=0)
    ext_property = db.Column(db.JSON, default={})
    is_available = db.Column(db.INT, default=1)
    create_ts = db.Column(db.TIMESTAMP, default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP, default=datetime.now())

    @classmethod
    def statistics_visitor(cls):
        VL = VisitorLog
        #  res = VL.query(VL.md5, func.count(VL.md5)).group_by(VL.md5).all()
        query_day = date.today()
        sql = 'is_bot = 0 and is_available = 1 and url like "%wxnacy.com%" and\
            visit_date = :date'
        res = db.session.query(VL.md5, func.count(VL.md5)).filter(text(sql)
            ).params(date = query_day).group_by(VL.md5).all()
        uv = len(res)
        pv = sum([o[1] for o in res])

        item = cls.query_item(visit_date = query_day)
        if not item:
            item = cls.create(visit_date = query_day)
        item.pv = pv
        item.uv = uv
        item.update_self()
        logger.debug('statistics_visitor %s', item)

class Test(BaseModel, db.Model):
    __tablename__ = 'test'
    id = db.Column(db.INT,primary_key=True)
