#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''生成md文件'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import os
import sys
from datetime import date

if __name__ == '__main__':
    args = sys.argv
    print(args)
    if len(args) < 4:
        raise Exception('参数有误')

    category = args[1]
    name = args[2]
    title = args[3]

    path_root = '{}/articles'.format(os.getcwd())

    file_name = '{}-{}-{}'.format(category, date.today().isoformat(), name)

    file_path = '{}/{}.md'.format(path_root, file_name)

    is_exists = os.path.exists(file_path)
    if is_exists:
        raise Exception("文件已经存在")

    file = open(file_path, '+w')
    file.write('# {}'.format(title))

    print('文件创建成功:{}'.format(file_path))
    print('地址:/{}/{}/{}'.format(category,
                                date.today().isoformat().replace('-', '/'),
                                name))
