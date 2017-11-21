#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from flask import Blueprint
import re

RE_DATE = re.compile('\d{4}/\d{2}/\d{2}')

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/visit', methods=['POST'])
def visit():
    ''''''
    return BaseResponse.return_success()
