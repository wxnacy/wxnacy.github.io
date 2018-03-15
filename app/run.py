#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''公共需要run的项目'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.common.base import BaseRequest
from app.config import app
from app.config import db
from app.config import BaseConfig
from app.config import logger
from app.models import Article


from app.views.index import index_bp
from app.views.api import api_bp
from app.views.code import code_bp
from flask import g
from flask import request
from flask_restless import APIManager
from datetime import datetime
import traceback
import time
import os


@app.before_request
def before_request():
    g.request_start_time = time.time()
    content_type = request.content_type or ''
    if 'application/x-www-form-urlencoded' in content_type:
        _args = request.form
    elif 'application/json' in content_type:
        _args = request.json
    else:
        _args = request.args
    logger.debug(
        '{}_{} begin \nargs:{}\ndata:{}\nheaders:\n{}'.format(
            request.method, request.url, _args,
            request.data, ''.join(
                ['header {}: {}\n'.format(k, v) for k, v in
                 request.headers])
        )
    )
    g.ip = request.remote_addr
    categorys = [
            dict(category='category',name='分类')
            ]
    g.categorys = []
    cate_html = []
    for cg in categorys:
        cate_html.append(
            '<li><a href="/{}">{}</a></li>'.format(cg[ 'category' ], cg[ 'name' ]))

    g.header = '<span><a href="/">wxnacy 博客 </a></span><nav><ul>{}</ul></nav>'.format(
    ''.join(cate_html))
    g.footer = ' © 2017 wxnacy.com 版权所有 <a href="http://www.miitbeian.gov.cn/" target="_blank">京ICP备15062634号-3</a>'


@app.after_request
def after_request(response):
    if not hasattr(g, 'request_start_time'):
        return response
    elapsed = datetime.utcnow().timestamp() - g.request_start_time
    req_info = '{}_{} end time_used:{}'.format(
        request.method,
        request.url, elapsed
    )
    logger.debug(req_info)
    return response

# api
app.register_blueprint(index_bp)
app.register_blueprint(api_bp)
app.register_blueprint(code_bp, url_prefix='/api/v1')

# restful
URL_PREFIX = '/api/restful' # BaseConfig.APPLICATION_ROOT_RESTFUL
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Article, url_prefix=URL_PREFIX, methods=['GET','POST'])


@app.errorhandler(Exception)
def app_error_handler(e):
    app.logger.error(traceback.format_exc())
    return BaseResponse.return_internal_server_error(str(e))
