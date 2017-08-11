#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wenxiaoning(371032668@qq.com)"
__copyright__ = "Copyright of hopapapa (2017)."

from app.common.base import BaseRequest
from app.config import BaseConfig
from app.run import app
from app.views.index import index_bp
from flask import g
from flask import request
import time
import os


@app.before_request
def before_request():
    g.request_start_time = time.time()
    app.logger.debug(
        '{} {}\nargs:{}\ndata:{}\nheaders:{}'.format(
            request.method, request.url, BaseRequest.get_args(), request.data,
            request.headers
        )
    )
    # ip
    g.ip = request.remote_addr

    CATEGORYS = ['python', 'mysql', 'git', 'ansible', 'js', 'mac', 'algorithm']
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
    elapsed = time.time() - g.request_start_time
    # elapsed = int(round(1000 * elapsed))
    app.logger.debug('{} begin request {} {} cast {} s'.format(
        g.request_start_time, request.method, request.url, elapsed
    ))

    return response


# api
app.register_blueprint(index_bp)
