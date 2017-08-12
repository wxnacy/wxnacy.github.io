#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.markdown import Markdown
from app.config import app
from app.config import BaseConfig
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import g
import os
import mistune

index_bp = Blueprint('index', __name__)
renderer = mistune.Renderer(escape=True, hard_wrap=True)
# use this renderer instance
md = mistune.Markdown(renderer=renderer)


@index_bp.route('/')
@index_bp.route('/index.html')
def index():
    '''首页'''
    article = []
    article.append('# {}'.format('wxnacy博客'))

    for c in g.categorys:
        article.append('\n')
        article.append(generator_category_md_content(c, 2))
    content = '\n'.join(article)
    md = Markdown(content=content)
    return render_template('index.html', article=md)


@index_bp.route('/<string:category>')
def category(category):
    '''文章分类'''
    content = generator_category_md_content(category, 1)
    md = Markdown(content=content)
    return render_template('index.html', article=md)


def generator_category_md_content(category, level):
    """生成分类文章md内容"""
    file_list = os.listdir(BaseConfig.ARTICLE_DIR)
    file_list = list(filter(lambda x: x.startswith(category), file_list))
    file_list.sort()
    article = []
    article.append('{} {}'.format('#' * level, category))
    for file in file_list:
        mf = Markdown(file)
        article.append('- [{}]({})'.format(mf.title, mf.route))
    return '\n'.join(article)


@index_bp.route(
    '/<string:category>/<string:year>/<string:month>/<string:day>/<string:name>')
def article(category, year, month, day, name):
    '''文章详情'''
    file = '{}-{}-{}-{}-{}.md'.format(category, year, month, day, name)
    md = Markdown(file)
    return render_template('index.html', article=md)
