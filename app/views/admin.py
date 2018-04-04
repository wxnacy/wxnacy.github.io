#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.common.base import BaseRequest
from app.config import BaseConfig
from app.models import User
from app.models import VisitorLog
from app.models import VisitorLogDate
from app.models import Article
from app.config import logger
from functools import wraps
from flask import Blueprint
from flask import url_for
from flask import render_template
from flask import redirect
from flask import request
from flask import make_response
from flask import g

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['POST', 'GET'])
def login():
    '''登陆'''
    method = request.method
    if method.lower() == 'get':
        return render_template('login.html')
    user = User.query_by_id(68719477421)
    res = make_response(redirect(url_for('admin.list_article')))
    res.set_cookie(BaseConfig.HEAD_AUTHORIZATION, user.generate_authorization())
    return res


@admin_bp.route('/index')
def index():
    args = dict(request.args) or {}
    visitors = VisitorLog.query_by(**args)
    return render_template('index.html', visitors=visitors)

@admin_bp.route('/visitor_log')
def list_visitor_log():
    args = BaseRequest.get_args()
    pagination = VisitorLog.query_by(**args)
    return render_template('admin/visitor_log_list.html', pagination=pagination)

@admin_bp.route('/article')
def list_article():
    args = BaseRequest.get_args()
    logger.debug(request)
    pagination = Article.query_by(**args)
    return render_template('admin/article_list.html', pagination=pagination)

@admin_bp.route('/visitor_log_date')
def list_visitor_log_date():
    args = BaseRequest.get_args()
    VisitorLogDate.statistics_visitor()
    pagination = VisitorLogDate.query_by(**args)
    return render_template('admin/visitor_log_date_list.html',
        pagination=pagination)

@admin_bp.route('/rank')
def rank():
    args = BaseRequest.get_args()
    rank = VisitorLog.query_rank(**args)
    return render_template('admin/rank.html',rank=rank)
