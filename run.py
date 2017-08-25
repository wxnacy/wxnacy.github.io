#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseRequest
from app.config import BaseConfig
from app.config import logger
from app.run import app
from app.views.index import index_bp
from datetime import datetime
from flask import g
from flask import request
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
    # ip
    g.ip = request.remote_addr

    logger.debug(g.ip)

    CATEGORYS = ['python', 'mysql', 'git', 'ansible', 'js', 'mac', 'algorithm',
                 'linux', 'html','openresty','shell']
    file_list = os.listdir(BaseConfig.ARTICLE_DIR)
    categorys = set([o.split('-', 1)[0] for o in file_list])
    categorys = list(filter(lambda x: x in CATEGORYS, categorys))
    categorys.sort()
    g.categorys = categorys
    print(categorys)

    cate_html = []
    for category in categorys:
        cate_html.append(
            '<li><a href="/{}">{}</a></li>'.format(category, category))

    g.header = '<span><a href="/">wxnacy博客</a></span><nav><ul>{}</ul></nav>'.format(
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
