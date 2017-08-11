#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.markdown import Markdown
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

    file_list = os.listdir(BaseConfig.ARTICLE_DIR)
    print(g.categorys)
    for c in g.categorys:

        fl = list(filter(lambda x: x.startswith(c), file_list))
        article.append('\n## {}'.format(c))
        for file in fl:
            mf = Markdown(file)
            article.append('- [{}]({})'.format(mf.title, mf.route))
    content = '\n'.join(article)
    md = Markdown(content=content)
    return render_template('index.html', article=md)


@index_bp.route('/<string:category>')
def category(category):
    '''文章分类'''
    file_list = os.listdir(BaseConfig.ARTICLE_DIR)
    file_list = list(filter(lambda x: x.startswith(category), file_list))

    article = []
    article.append('# {}'.format(category))
    for file in file_list:
        mf = Markdown(file)
        article.append('- [{}]({})'.format(mf.title, mf.route))

    content = '\n'.join(article)
    md = Markdown(content=content)
    return render_template('index.html', article=md)


@index_bp.route(
    '/<string:category>/<string:year>/<string:month>/<string:day>/<string:name>')
def article(category, year, month, day, name):
    '''文章详情'''
    file = '{}-{}-{}-{}-{}.md'.format(category, year, month, day, name)
    md = Markdown(file)
    return render_template('index.html', article=md)
