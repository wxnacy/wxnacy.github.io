#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.config import logger
from app.models import AutoId
from app.models import VisitorLog
from app.models import Article
from functools import wraps
from flask import Blueprint
from flask import request
import json

api_bp = Blueprint('api', __name__)


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

#  @api_bp.route('/article/<string:url>', methods=['PUT'])
#  def crawler_article(url):
    #  '''更新文章'''
    #  res = Article.crawler(url=url)
    #  return BaseResponse.return_success(res.format())

@api_bp.route('/test', methods=['POST', 'GET'])
def test():
    '''测试'''
    req = f'''
        path: {request.path}
        url: {request.url}
    '''
    res = dict(request=req)
    return BaseResponse.return_success(res)
