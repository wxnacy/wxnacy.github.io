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
from app.models import User
from app.models import Nav
from app import models
from app.schema import schema


from app.views.index import index_bp
from app.views.api import api_bp
from app.views.code import code_bp
from flask import g
from flask import request
from flask import redirect
from flask_restless import APIManager
from flask_graphql import GraphQLView
from datetime import datetime

import traceback
import time
import os
import inspect
import importlib



@app.before_request
def before_request():
    g.request_start_time = time.time()
    try:
        data = request.data
        logger.debug('data   %s', data)
        args = request.args or {}
        logger.debug('args   %s', args)
        json_data = request.json or {}
        logger.debug('json   %s', json_data)
        form_data = request.form or {}
        logger.debug('form   %s', form_data)
        h_data = request.headers or {}
        for k, v in h_data:
            logger.debug('header %s: %s', k, v)
    except Exception as e:
        logger.error('params %s', e)
        logger.error(traceback.format_exc())

    navs = Nav.query_items()
    g.navs = navs
    g.current_nav = Nav.query_item(url=request.path)

    authorization = request.cookies.get('authorization')
    if not authorization:
        user = None
    else:
        user = User.get_user_from_authorization(authorization)

    if request.path.startswith('/admin'):
        if not user and (request.path != '/admin/login' or request.path.startswith('/static')):
            return redirect('/admin/login')

    g.current_user = user



@app.after_request
def after_request(response):
    if not hasattr(g, 'request_start_time'):
        return response
    elapsed = time.time() - g.request_start_time
    logger.debug('end    time_used: %s', elapsed)
    return response

# api

views_path = '{}/app/views/'.format(os.getcwd())
logger.debug(views_path)
views_files = list(filter(
    lambda x: not x.startswith('__') and '.swp' not in x and '.swo' not in x,
    os.listdir(views_path)))
for path in views_files:
    module_name = 'app.views.{}'.format(path[0:-3])
    views_module = importlib.import_module(module_name)
    for name, obj in inspect.getmembers(views_module):
        if obj.__class__.__name__ == 'Blueprint':
            url_prefix = '/api/v1'
            if name == 'admin_bp':
                url_prefix = '/admin'
            app.register_blueprint(obj, url_prefix = url_prefix)

# restless
manager = APIManager(app, flask_sqlalchemy_db=db)
restful_params = dict(
    methods=['GET'],
    results_per_page=10,
    allow_functions=True,
    url_prefix = '/api/restless'
)

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj) and '__tablename__' in dir(obj):
        manager.create_api(obj, **restful_params)

''' for graphql'''
app.add_url_rule('/api/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.errorhandler(Exception)
def app_error_handler(e):
    app.logger.error(traceback.format_exc())
    return BaseResponse.return_internal_server_error(str(e))


