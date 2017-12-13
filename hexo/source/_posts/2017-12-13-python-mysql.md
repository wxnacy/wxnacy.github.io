---
title: Python 操作 Mysql
date: 2017-12-13 18:47:16
tags: [python, mysql]
---

在 Python 中有很多可以操作 Mysql 的模块，在这里简单介绍下 `pymysql` 模块
<!-- more -->

## pymysql
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import pymysql
from urllib.parse import urlparse

url = 'mysql+pymysql://root:password@localhost:3306/db?charset=utf8mb4'
URL_CONFIG = urlparse(url)

class BaseDB(object):
    @classmethod
    def create_conn(cls):
        '''创建mysql链接'''
        return pymysql.connect(
            host=URL_CONFIG.hostname,
            port=URL_CONFIG.port,
            user=URL_CONFIG.username,
            password=URL_CONFIG.password,
            db=URL_CONFIG.path[1:],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    @classmethod
    def query(cls, sql, params):
        """
        查询操作
        :param sql:
        :param params:
        :return:
        """
        conn = cls.create_conn()
        try:
            cursor = conn.cursor()      # 获取操作游标

            cursor.execute(sql, params) # 执行 sql 语句
            conn.commit()               # 提交
            result = cursor.fetchall()  # 查询语句获取所以数据
            cursor.close()              # 关闭游标
            return result
        except BaseException as e:
            return []
        finally:
            conn.close()                # 关闭连接

    @classmethod
    def execute(cls, sql, params):
        """
        更新操作
        :param sql:
        :param params:
        :return:
        """
        conn = cls.create_conn()
        try:
            cursor = conn.cursor()

            result = cursor.execute(sql, params)
            conn.commit()
            cursor.close()
            return result
        except BaseException as e:
            return False
        finally:
            conn.close()


if __name__ == "__main__":
    db = BaseDB()
    # 需要传递的参数使用 %s 替换
    sql = "insert into test_user(id, name) values (%s, %s);"
    # 参数放在数组中
    db.execute(sql, [1, 'wxnacy'])
    sql = "select * from test_user;"
    res = db.query(sql, [])
    print(res)      # ==> [{"id":1, "name": "wxnacy"}]
```
