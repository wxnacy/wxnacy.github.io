#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.config import logger
from app.models import AutoId
from app.models import VisitorLog
from functools import wraps
from flask import Blueprint
from flask import request
import json
from user_agents import parse

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
    ua = parse(ua)
    args['os'] = ua.os.family
    args['device'] = ua.device.family
    args['browser'] = ua.browser.family
    device_type = 'pc'
    if ua.is_mobile:
        device_type = 'mobile'
    elif ua.is_tablet:
        device_type = 'tablet'
    args['device_type'] = device_type
    #  args['is_bot'] = 1 if ua.is_bot else 0
    args['is_bot'] = ua.is_bot
    logger.debug(args)
    res = VisitorLog.create(**args)
    return BaseResponse.return_success(res.format())
