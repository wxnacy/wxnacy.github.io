#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.models import VisitUser as VU
from functools import wraps
from flask import Blueprint

api_bp = Blueprint('api', __name__)

def visit_log(func):
    @wraps(func)
    def _w(*args, **kwargs):
        VU.log()
        return func(*args, **kwargs)
    return _w

@api_bp.route('/api/visit', methods=['POST'])
@visit_log
def visit():
    ''''''
    return BaseResponse.return_success()
