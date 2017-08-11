#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import sqlparse



if __name__ == '__main__':
    sql = 'select * from `user`';
    sql = 'create table `user`(\n' \
          '  id int(11) not null auto_increment' \
          ')engine=InnoDB default charset=utf8mb4 ;'
    res = sqlparse.format(sql,reindent=True,keyword_case='upper',output_format='python')
    print(res)