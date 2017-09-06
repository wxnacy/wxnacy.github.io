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

def visit_log(func):
    @wraps(func)
    def _w(*args, **kwargs):
        VU.log()
        return func(*args, **kwargs)

    return _w


@index_bp.route('/')
@index_bp.route('/index.html')
@visit_log
def index():
    '''首页'''
    article = []
    #  article.append('# {}'.format('wxnacy博客'))

    #  for c in g.categorys:
        #  article.append('\n')
        #  article.append(generator_category_md_content(c, 2))
    #  content = '\n'.join(article)
    #  md = Markdown(content=content)
    md = Article.get_timeline_md()

    return render_template('index.html', article=md)


@index_bp.route('/<string:category>')
@visit_log
def category(category):
    '''文章分类'''
    if category == 'category':
        md = Category.get_categorys_md()
    else:
        md = Category.get_md(category,1)
    return render_template('index.html', article=md)

@index_bp.route(
    '/<string:category>/<string:year>/<string:month>/<string:day>/<string:name>')
@visit_log
def article(category, year, month, day, name):
    '''文章详情'''
    file = '{}-{}-{}-{}-{}.md'.format(category, year, month, day, name)
    md = Markdown(file)
    return render_template('index.html', article=md)


@index_bp.route('/test', methods=['POST', 'GET'])
def test():
    res = {
        'headers': dict(request.headers),
        'args': request.args,
        'json': request.json,
        'form': request.form,
        'data': str(request.data)
    }

    return jsonify(res)
