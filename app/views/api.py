#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.common.wx_utils import WXSecurity
from app.common.wx_utils import Message
from app.common.decorator import args_required
from app.common.decorator import response_xml
from app.config import BaseConfig
from app.config import logger
from app.models import AutoId
from app.models import User
from app.models import VisitorLog
from app.models import Article
from functools import wraps
from flask import Blueprint
from flask import request
import json

api_bp = Blueprint('api', __name__)

wxs = WXSecurity()


@api_bp.route('/auto_id/<int:shard_id>/<int:item_id>', methods=['POST'])
def create_auto_id(shard_id, item_id):
    '''生成id'''
    id = AutoId.generate_id(shard_id, item_id)
    return BaseResponse.return_success({"id": id})

@api_bp.route('/visitor_log', methods=['POST'])
def create_visitor_log():
    '''生成访问记录'''
    args = request.json
    headers = request.headers
    ua = headers.get('user_agent')
    args['user_agent'] = ua
    res = VisitorLog.visit(**args)
    return BaseResponse.return_success(res.format())

@api_bp.route('/article/<int:id>', methods=['PUT'])
def update_article(id):
    '''更新文章'''
    res = Article.query_by_id(id)
    res.crawler_self()
    return BaseResponse.return_success(res.format())

@api_bp.route('/article', methods=['post'])
def crawler_article():
    '''创建'''
    args = request.json
    url = args['url']
    res = Article.crawler(url=url)
    return BaseResponse.return_success(res.format())

@api_bp.route('/login', methods=['post'])
@args_required('email', 'password')
def login():
    '''登录'''
    args = request.json
    s, item = User.login(**args)
    if s != 200:
        return BaseResponse.return_response(status=s, message=item)
    return BaseResponse.return_response(data = item, headers = {
        BaseConfig.HEAD_AUTHORIZATION: item.authorization
        })

@api_bp.route('/register', methods=['post'])
@args_required('email', 'password')
def register():
    '''注册'''
    args = request.json
    s, item = User.register(**args)
    if s != 200:
        return BaseResponse.return_response(status=s, message=item)
    return BaseResponse.return_response(data = item, headers = {
        BaseConfig.HEAD_AUTHORIZATION: item.authorization
    })

@api_bp.route('/wx/mp_callback', methods=['POST', 'GET', 'PUT', "DELETE"])
@response_xml
def wx_callback():
    '''测试'''
    method = request.method
    logger.debug(method)
    if method == "GET":
        args = request.args
        if wxs.check_request(signature = args['signature'],
                timestamp = args['timestamp'], nonce = args['nonce']):
            return request.args.get('echostr', 'success')
        else:
            return 'error'

    if method == "POST":
        s, res = Message.decrypt_body(request.data)
        if s == 200:
            msg = Message(res)
            return msg.reply_text(msg.content)
        else:
            return msg.reply_text(res)

    return ''

@api_bp.route('/wapi/test', methods=['POST', 'GET', 'PUT', "DELETE"])
def wapi_test():
    '''测试'''
    res = {}
    res.update(dict(path= request.path))
    res.update(dict(method= request.method))
    res.update(dict(args= request.args))
    res.update(dict(json= request.json))
    res.update(dict(form= request.form))
    res.update(dict(headers= dict(request.headers)))
    return BaseResponse.return_success(res)
