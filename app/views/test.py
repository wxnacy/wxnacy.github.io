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

index_bp = Blueprint('test', __name__)

#  def visit_log(func):
    #  @wraps(func)
    #  def _w(*args, **kwargs):
        #  VU.log()
        #  return func(*args, **kwargs)
    #  return _w

#  @index_bp.route('/')
#  @index_bp.route('/index.html')
#  @visit_log
#  def index():
    #  '''首页'''
    #  article = []
    #  md = Article.get_timeline_md()
    #  return render_template('index.html', article=md)

#  @index_bp.route('/<string:name>')
#  @visit_log
#  def route_one(name):
    #  '''文章分类'''
    #  cg = Category.query_item(name=name)
    #  md = Markdown(content=cg.content)
    #  return render_template('index.html', article=md)

#  @index_bp.route('/category')
#  @visit_log
#  def category_list():
    #  '''文章分类'''
    #  md = Category.get_categorys_md()
    #  return render_template('index.html', article=md)

#  @index_bp.route('/search')
#  @visit_log
#  def search():
    #  '''搜索'''
    #  q = request.args['q']
    #  md = Article.search(q)
    #  return render_template('index.html', article=md)

#  @index_bp.route(
    #  '/<string:category>/<string:year>/<string:month>/<string:day>/<string:name>')
#  @visit_log
#  def article(category, year, month, day, name):
    #  '''文章详情'''
    #  file = '{}-{}-{}-{}-{}.md'.format(category, year, month, day, name)
    #  md = Markdown(file)
    #  return render_template('index.html', article=md)


#  @index_bp.route('/test', methods=['POST', 'GET'])
#  def test():
    #  res = {
        #  'method': request.method,
        #  'headers': dict(request.headers),
        #  'args': request.args,
        #  'json': request.json,
        #  'form': request.form,
        #  'data': str(request.data),
        #  'addr': request.path
    #  }

    #  return jsonify(res)
