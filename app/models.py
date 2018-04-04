#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''models'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseModel as BM
from app.common.base import BaseDB
from app.common.md import Markdown
from app.common.security import Md5
from app.common.security import AESecurity
from app.config import db
from app.config import BaseConfig
from app.config import logger
from datetime import datetime
from datetime import date
from datetime import timedelta
from sqlalchemy.orm import backref as b
from sqlalchemy import desc
from sqlalchemy import or_
from sqlalchemy import text
from sqlalchemy import func
from flask import request
from user_agents import parse
import os
import re
import json
import subprocess
import requests
import time
import traceback
from bs4 import BeautifulSoup

aes = AESecurity(BaseConfig.AES_KEY)


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


    def generate_authorization(self):
        return aes.encrypt(f'{self.id};')

    @classmethod
    def get_user_from_authorization(cls, authorization):
        try:
            plain = aes.decrypt(authorization)
            if ';' not in plain:
                return None
        except:
            logger.error(traceback.format_exc())
            return None
        id = plain.split(';')[0]
        return cls.query_by_id(id)



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
    def query_rank(cls, **kw):
        logger.debug(kw)
        qd = date.today()
        if 'day' in kw:
            qd = kw['day']

        res = db.session.query(cls.url, func.count(cls.url).label('rank')
            ).filter(cls.visit_date == qd
            ).group_by(cls.url).order_by('rank desc').all()

        return res

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

        def _statistics(query_day):

            VL = VisitorLog
            #  res = VL.query(VL.md5, func.count(VL.md5)).group_by(VL.md5).all()
            sql = 'is_bot = 0 and is_available = 1 and url like :url and\
                visit_date = :date'
            res = db.session.query(VL.md5, func.count(VL.md5)).filter(text(sql)
                    ).params(date = query_day, url='https://wxnacy.com%').group_by(VL.md5).all()
            uv = len(res)
            pv = sum([o[1] for o in res])

            item = cls.query_item(visit_date = query_day)
            if not item:
                item = cls.create(visit_date = query_day)
            item.pv = pv
            item.uv = uv
            item.update_self()
            logger.debug('statistics_visitor %s', item)

        query_day = date.today()
        _statistics(query_day)
        query_day = date.today() - timedelta(days=1)
        _statistics(query_day)


class Article(BaseModel,db.Model):
    __tablename__ = 'article'
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.String,default="")
    url = db.Column(db.String, default="")
    publish_date = db.Column(db.DATE, default = '2017-08-04')
    tag = db.Column(db.String,default="")
    pv = db.Column(db.INT,default=0,doc="观看数量")
    init_pv = db.Column(db.INT,default=0,doc="初始值")
    ext_property = db.Column(db.JSON,default={})
    is_available = db.Column(db.INT,default=1)
    create_ts = db.Column(db.TIMESTAMP,default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP,default=datetime.now())

    DOMAIN = 'https://wxnacy.com'


    @classmethod
    def query_or_create(cls, url, **kw):
        if not url.startswith('https://wxnacy.com'):
            return None
        if url == 'https://wxnacy.com' or url == 'https://wxnacy.com/':
            return None
        if url.startswith('https://wxnacy.com/archives'):
            return None
        if url.startswith('https://wxnacy.com/page'):
            return None
        if '?' in url:
            url = url[0:url.index('?')]
        if '#' in url:
            url = url[0:url.index('#')]
        if url.endswith('index.html'):
            url = url[0:url.index('index.html')]

        kw['url'] = url
        print(url)
        return super().query_or_create(**kw)


    @classmethod
    def crawler(cls, url, **kw):
        item = cls.query_or_create(url=url)
        if not item:
            return None
        params = cls.get_crawler_data(url)

        cls.update_by_id(item.id, **params)
        return item

    def crawler_self(self):
        params = Article.get_crawler_data(self.url)
        print(params)
        Article.update_by_id(self.id, **params)
        return self

    @classmethod
    def crawler_article(cls):

        def _crawler(url):
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')
            items = soup.find_all('a', class_='article-title')
            for item in items:
                item_url = '{}{}'.format(cls.DOMAIN, item.attrs['href'])
                print(item_url)
                cls.crawler(url=item_url)

        for i in range(23):
            if i == 0:
                url = 'https://wxnacy.com'
            else:
                url = '{}/page/{}'.format(cls.DOMAIN, i+1)
            _crawler(url)

    def create_init_pv(self):
        jc = "BusuanziCallback_768395723167"
        url = "https://busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback_768395723167"
        res = requests.get(url, headers=dict(referer=self.url))
        suffix = ');}catch(e){}'
        prefix = 'try{BusuanziCallback_768395723167('
        text = res.content.decode('utf-8')
        if text.startswith(prefix) and text.endswith(suffix):
            json_text = text[text.index(prefix)+len(prefix):text.index(suffix)]
            res = json.loads(json_text)
            print(res)
            print(res.get('page_pv', 0))
            self.init_pv = res.get('page_pv', 0)
            print(self.init_pv)
            self.update_self()

    @classmethod
    def statistics_init_pv(cls):
        items = Article.query_items(init_pv = 0)
        print(len(items))
        for item in items:
            item.create_init_pv()

    @classmethod
    def statistics_article(cls):
        begin = time.time()
        items = Article.query_items()
        for item in items:
            item.crawler_self()

        logger.debug('statistics_article time: %s', (time.time() - begin))


    @classmethod
    def get_crawler_data(cls, url):
        params = {}
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        metas = soup.find_all('meta')
        pd = '2017-08-04'
        for meta in metas:
            attrs = meta.attrs
            if attrs.get('property') == 'og:title':
                params['name'] = attrs['content']
            elif attrs.get('name') == 'keywords':
                params['tag'] = attrs['content']
            elif attrs.get('property') == 'og:updated_time':
                pd = attrs['content'][0:10]

        dp = url.split('/')
        if len(dp) > 5:
            pd = '{}-{}-{}'.format(dp[3], dp[4], dp[5])
        params['publish_date'] = pd
        print(params)
        return params



    @classmethod
    def statistics_pv(cls):
        items = cls.query_items()
        AD = ArticleData
        for item in items:
            ArticleData.query_items(article_id=item.id)
            res = db.session.query(func.sum(AD.pv)).filter_by(article_id=item.id).all()
            if res[0][0]:
                item.pv = res[0][0]
                db.session.add(item)
        db.session.commit()




class Nav(BaseModel,db.Model):
    __tablename__ = 'nav'
    id = db.Column(db.BIGINT,primary_key=True)
    name = db.Column(db.String,default="")
    url = db.Column(db.String, default="")
    ext_property = db.Column(db.JSON,default={})
    is_available = db.Column(db.INT,default=1)
    create_ts = db.Column(db.TIMESTAMP,default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP,default=datetime.now())

class ArticleData(BaseModel, db.Model):
    __tablename__ = 'article_data'
    id = db.Column(db.INT, primary_key=True)
    article_id = db.Column(db.INT, db.ForeignKey('article.id'))
    visit_date = db.Column(db.Date, default = date.today)
    pv = db.Column(db.INT, default=0)
    uv = db.Column(db.INT, default=0)
    ext_property = db.Column(db.JSON, default={})
    is_available = db.Column(db.INT, default=1)
    create_ts = db.Column(db.TIMESTAMP, default=datetime.now())
    update_ts = db.Column(db.TIMESTAMP, default=datetime.now())

    @classmethod
    def statistics_article_data(cls):

        def _statistics(vd):
            begin = time.time()
            VL = VisitorLog
            items = db.session.query(VL.url, func.count(VL.url)
                ).filter(VL.visit_date == vd).group_by(VL.url).all()
            for item in items:
                article = Article.query_or_create(url=item[0])
                if article:
                    ad = cls.query_or_create(article_id=article.id,
                        visit_date=vd)
                    ad.pv = item[1]
                    db.session.add(ad)
            db.session.commit()

            logger.debug('statistics_article_data time: %s',
                    (time.time() - begin))

        vd = date.today()
        _statistics(vd)
        vd = date.today() - timedelta(days=1)
        _statistics(vd)

class Test(BaseModel, db.Model):
    __tablename__ = 'test'
    id = db.Column(db.INT,primary_key=True)
