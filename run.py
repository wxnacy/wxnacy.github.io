#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wenxiaoning(371032668@qq.com)"
__copyright__ = "Copyright of hopapapa (2017)."

from app.common.base import BaseRequest
from app.config import BaseConfig
from app.run import app
from app.views.api.user import user_bp
from app.views.api.wx import wx_bp
from flask import g
from flask import request
import time


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
URL_PREFIX = BaseConfig.APPLICATION_ROOT
app.register_blueprint(user_bp, url_prefix=URL_PREFIX)
app.register_blueprint(wx_bp, url_prefix=URL_PREFIX)
