#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from app.models import VisitorLog
from app.models import Article

def print_hot():
    items = VisitorLog.query_hot()
    def _filter(o):
        if o.url in ('https://wxnacy.com/',
                'https://wxnacy.com/tool/',
                'https://wxnacy.com/album/',
                ):
            return False
        if o.url.startswith('http://local.wxnacy.com') or \
                o.url.startswith('http://localhost'):
            return False
        return True
    items = list(filter(lambda x: _filter(x), items))
    items = items[0:10]

    for i in items:
        if 'vim.wxnacy.com' in i.url:
            print('VIM 练级手册: ', i.url)
            continue
        art = Article.query_item(url = i.url)
        if not art:
            art = Article.crawler(url = i.url)
        url = i.url
        if url.startswith('https://wxnacy.com'):
            url = url[len('https://wxnacy.com'):]
        fmt = '{}: {}'.format(art.name, url)
        print(fmt)
    pass

if __name__ == "__main__":
    print_hot()
     
