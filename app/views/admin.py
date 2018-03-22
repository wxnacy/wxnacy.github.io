#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.models import User
from app.config import logger
from functools import wraps
from flask import Blueprint
from flask import url_for
from flask import render_template
from flask import redirect
from flask import request
from flask import make_response
from flask import g

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['POST', 'GET'])
def login():
    '''登陆'''
    method = request.method
    if method.lower() == 'get':
        return render_template('login.html')

    user = User.query_by_id(68719477421)
    g.current_user = user
    logger.debug(g.current_user)
    res = make_response(render_template('index.html'))
    res.set_cookie('name', user.name)
    return res


@admin_bp.route('/index')
def index():
    logger.debug(g.current_user)
    return render_template('index.html')

