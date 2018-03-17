#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.models import AutoId
from functools import wraps
from flask import Blueprint

api_bp = Blueprint('api', __name__)


@api_bp.route('/auto_id/<int:shard_id>/<int:item_id>', methods=['POST'])
def create_auto_id(shard_id, item_id):
    '''生成id'''
    id = AutoId.generate_id(shard_id, item_id)
    return BaseResponse.return_success({"id": id})
