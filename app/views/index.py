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
import mistune
import re

RE_DATE = re.compile('\d{4}/\d{2}/\d{2}')

index_bp = Blueprint('index', __name__)
renderer = mistune.Renderer(escape=True, hard_wrap=True)
# use this renderer instance
md = mistune.Markdown(renderer=renderer)


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
    content = generator_category_md_content(category, 1)
    md = Markdown(content=content)
    if category == 'category':
        md = Category.get_categorys_md()
    return render_template('index.html', article=md)


def generator_category_md_content(category, level):
    """生成分类文章md内容"""
    file_list = os.listdir(BaseConfig.ARTICLE_DIR)
    file_list = list(filter(lambda x: x.startswith(category), file_list))
    file_list = list(filter(lambda x: 'item' not in x, file_list))
    file_list.sort()
    article = []
    article.append('{} {}'.format('#' * level, category))
    items = []
    for file in file_list:
        mf = Markdown(file)
        profix = '专辑' if 'album' in mf.route else '文章'
        res = re.findall(RE_DATE, mf.route)
        date = ''
        if res:
            date = res[0]
        items.append(
            '- {} [{}] [{}]({})'.format(date, profix, mf.title, mf.route))
        items.sort(reverse=True)
    article.extend(items)

    return '\n'.join(article)


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
