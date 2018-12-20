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
        return True
    items = list(filter(lambda x: _filter(x), items))
    items = items[0:5]

    for i in items:
        art = Article.crawler(url = i.url)
        fmt = '{}: {}'.format(art.name, art.url)
        print(fmt)
    pass

if __name__ == "__main__":
    print_hot()
     
