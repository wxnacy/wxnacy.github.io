#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.config import logger
from app.models import Code
from app.models import User
from flask import Blueprint
from flask import request
from flask import g

code_bp = Blueprint('code', __name__)


@code_bp.route('/code', methods=['POST'])
def create_code():
    '''创建代码'''
    if not g.current_user:
        return BaseResponse.return_unauthorized('请先登录')
    args = request.json
    item = Code.create_or_update(**args)
    return BaseResponse.return_success(item.format())

@code_bp.route('/code/<string:id>', methods=['GET'])
def code_detail(id):
    '''获取详情'''

    item = Code.query_by_id(id)
    return BaseResponse.return_success(item.format())
