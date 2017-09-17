#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy
# Email: wxnacy@gmail.com
# Description:

from app.config import BaseConfig
from app.common import utils
import os
import re

FILE_LIST = os.listdir(BaseConfig.ARTICLE_DIR)
FILE_LIST = list(filter(lambda x: not x.startswith('.'),FILE_LIST))

HEXO_HOME = '/Users/wxnacy/WebstormProjects/wxnacy.github.io/hexo/source/_posts/'
POST_LIST= os.listdir(HEXO_HOME)
POST_LIST = list(filter(lambda x: not x.startswith('.'),POST_LIST))


RE_DATE = re.compile(u"\d{4}-\d{2}-\d{2}")  # 正则时间类型

def dump():

    fl = FILE_LIST

    #  fn = 'mysqjjjl/2017/09/15/tmp-mysql-sock'
    #  fn = fn.replace('/','-')
    #  fl = list(filter(lambda x: fn in x, fl))
    #  fl.re
    rl = [
            #  'algorithm-2017-08-05-identity_verify.md',
            #  'ansible-2017-08-08-item-basic_playbooks_ext.md',
            'ansible-2017-08-08-item-basic_tasks1.md',
            #  'python-2017-08-15-album-build-project.md',
            'python-2017-08-10-pyenv-mac.md'
            ]
    fl = [x for x in FILE_LIST if x not in POST_LIST and x not in rl]
    print(fl)
    print(fl[0])
    for f in fl:
        tag = f.split('-')[0]
        res = re.findall(RE_DATE, f)
        d = ''
        if res:
            d = res[0]
        path = BaseConfig.ARTICLE_DIR + f
        rf = open(path,'r')
        res = rf.read()
        line = res.split('\n')
        title = line[0][2:]
        line.pop(0)
        data = ['---\ntitle: {}\ndate: {}\ntags: [{}]\n---\n'.format(title,
            d,tag)]
        data.extend(line)
        #  wf = open('/data/_posts/{}'.format(f),'w')
        #  wf = open('/Users/wxnacy/WebstormProjects/wxnacy.blog/source/_posts/{}'.format(utils.get_random_str(4)+'.md'),'w')
        wf = open('{}{}'.format(HEXO_HOME,f),'w')
        wf.write('\n'.join(data))
        wf.close()
        rf.close()
    pass



if __name__ == '__main__':
    dump()

