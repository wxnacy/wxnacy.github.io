#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.models import Code
from flask import Blueprint
from flask import request

code_bp = Blueprint('code', __name__)


@code_bp.route('/code', methods=['POST'])
def create_code():
    '''创建代码'''
    args = request.json
    args['id'] = Code.generate_id()
    item = Code.create(**args)
    return BaseResponse.return_success(item.format())

@code_bp.route('/code/<string:id>', methods=['GET'])
def code_detail(id):
    '''获取详情'''

    item = Code.query_by_id(id)
    return BaseResponse.return_success(item.format())
