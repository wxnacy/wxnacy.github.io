#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''views'''
__author__ = "wenxiaoning(371032668@qq.com)"
__copyright__ = "Copyright of pythondemo (2017)."

from app.models import Article
from flask import Blueprint
from flask import render_template
from flask import url_for

article_bp = Blueprint('article', __name__)

KEY = 'ab60373552d9daa6'


@article_bp.route('/')
@article_bp.route('/article/<string:category>.html')
def article_list(category):
    '''首页'''
    return render_template('www/pages/article/list.html',
                           items=Article.query_items(category=category),
                           **mark_res())


@article_bp.route('/article/<string:id>.html')
def article_detail(id):
    '''视频详情'''
    return render_template('www/pages/article/detail.html',
                           item=Article.query_item(id=id),
                           **mark_res())


def make_categorys(*args):
    if not args:
        args = ['java', 'python']
    return [dict(name=o, url=url_for('article.article_list',
                                     category=o)) for o in args]


def mark_res():
    return dict(
        categorys=make_categorys(),
        new_items=Article.query_items()
    )
