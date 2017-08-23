#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''models'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseModel
from app.common.security import Md5
from app.config import db
from datetime import datetime
from sqlalchemy.orm import backref as b
from flask import request


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
        print('{};{}'.format(ip, user_agent))
        return Md5.encrypt('{};{}'.format(ip, user_agent))

    @classmethod
    def log(cls):
        headers = request.headers
        print(headers)
        ip = request.remote_addr
        user_agent = request.user_agent
        print(type(str(user_agent)))

        md5 = cls.generate_md5(ip, user_agent)
        print(md5)
        user = cls.query_item(md5=md5)
        if not user:
            user = cls(ip=ip, user_agent=str(user_agent), md5=md5,
                              ext=dict(headers))
            user.create_self()
        return user.visit()

    def visit(self):
        print(request.referrer)
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
