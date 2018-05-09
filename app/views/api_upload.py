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

app_bp = Blueprint('upload', __name__)


@app_bp.route('/upload', methods=['POST'])
def upload():
    '''创建代码'''
    logger.debug(request.files)
    return BaseResponse.return_success()

