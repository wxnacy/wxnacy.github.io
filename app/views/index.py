#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.md import Markdown
from app.config import app
from app.config import BaseConfig
from app.models import VisitUser as VU
from app.models import Category
from app.models import Article
from flask import Blueprint
from flask import render_template
from flask import request
from flask import g
from flask import jsonify
from functools import wraps
import os
import re

RE_DATE = re.compile('\d{4}/\d{2}/\d{2}')

index_bp = Blueprint('index', __name__)

#  def visit_log(func):
    #  @wraps(func)
    #  def _w(*args, **kwargs):
        #  VU.log()
        #  return func(*args, **kwargs)
    #  return _w

#  @index_bp.route('/json')
#  @visit_log
#  def index():
    #  '''首页'''
    #  article = []
    #  md = Article.get_timeline_md()
    #  return render_template('index.html', article=md)
