---
title: Flask Restless 20 行代码搞定服务器 CURD 接口
tags:
  - python
date: 2018-01-26 21:45:56
---


在使用 Flask 开发 web 接口时，设计到简单 RESTful 风格接口，使用 Restless 插件会非常方便，只需要几行代码就可以搞定一个服务器接口

<!-- more --><!-- toc -->

## 下载
```bash
$ pip install Flask-Restless
```

## 快速开始
编辑 `run.py`
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.String, default="", doc='名称')


manager.create_api(Book, methods=['GET', 'POST', 'PUT', 'DELETE'])

app.run()
```
启动
```bash
$ python run.py
```
### POST
创建
```bash
$ curl -X POST localhost:5000/api/book -H "Content-Type:application/json" -d '{"name":"wxnacy"}'
```
```bash
{
    "id": 96,
    "name": "wxnacy"
}
```
### GET
查看列表
```bash
curl localhost:5000/api/book
```
```json
{
    "num_results": 95,
        "objects": [
        {
            "id": 2,
            "name": "2-book"

        },
        ...
        {
            "id": 11,
            "name": "wxnacy"

        }

        ],
        "page": 1,
        "total_pages": 10
}
```
查看单个
```bash
$ curl localhost:5000/api/book/96
```
```json
{
    "id": 96,
    "name": "wxnacy"
}
```
### PUT
```bash
$ curl -X PUT localhost:5000/api/book/96 -H "Content-Type:application/json" -d '{"name":"new_name"}'
```
```json
{
    "id": 96,
    "name": "new_name"
}
```
### DELETE
```bash
$ curl -X DELETE localhost:5000/api/book/96
```
看，几行代码就搞定了增删改查四大功能，如果你只是搭个自己的小服务，这就已经足够了，再也不用吭哧吭哧写代码了，关于 Methods 的更多解释见[文档 ](https://flask-restless.readthedocs.io/en/stable/customizing.html#http-methods)

## 修改地址前缀
```python
manager.create_api(Book, url_prefix='/api/v2', methods=['GET'])
```
在 `create_api` 的时候作如上改动，就可以修改接口前缀
```bash
$ curl localhost:5000/api/v2/book
```

## 搜索请求
Restless 非常强大的功能是，他可以在不改动代码的情况下做基于数据的条件查询
```bash
curl \
    -G \
    -H "Content-type: application/json" \
    -d "q={\"filters\":[{\"name\":\"name\",\"op\":\"like\",\"val\":\"%new%\"}]}" \
    http://127.0.0.1:5000/api/book
```
```json
{
    "num_results": 2,
    "objects": [
    {
        "id": 6,
        "name": "new book"
    },
    {
        "id": 7,
        "name": "new book"
    }],
    "page": 1,
    "total_pages": 1
}
```
什么代码都没动，就完成 `like` 的查询的操作，妈妈再也不用担心我写 API 了
### 请求格式
```json
{"name": <fieldname>, "op": <operatorname>, "val": <argument>}
```
或
```
{"name": <fieldname>, "op": <operatorname>, "field": <fieldname>}
```
`fieldname` 是字段名，`operatorname` 是查询条件，`argument` 是条件值，通过不同的 `op` 值来完成相应操作，更多的 Operators 值
- ==, 371032668@qq.com, equals, equals_to
- !=, neq, does_not_equal, not_equal_to
- `>, gt, <, lt`
- `>=, ge, gte, geq, <=, le, lte, leq`
- in, not_in
- is_null, is_not_null
- like
- has
- any
更多用法见[文档](https://flask-restless.readthedocs.io/en/stable/searchformat.html#query-format)

## 方法求值
Restless 另一个比较牛逼的功能，是可以使用数据库的函数，比如
```bash
$ curl localhost:5000/api/eval/book?q={"functions": [{"name": "count", "field": "id"}]}
# urlencode 编码后请求
$ curl localhost:5000/api/eval/book?q=%7B%22functions%22%3A%20%5B%7B%22name%22%3A%20%22count%22%2C%20%22field%22%3A%20%22id%22%7D%5D%7D
```
```json
{"count__id": 94}
```
就这样，我们得到了数据总和，不过这个功能默认是不打开的，需要设置 `allow_functions` 手动打开
```python
manager.create_api(Book, allow_functions=True, methods=['GET', 'POST', 'PUT', 'DELETE'])
```
更多介绍见[文档](https://flask-restless.readthedocs.io/en/stable/requestformat.html#function-evaluation)

## JSONP
Restless 默认支持 JSONP，使用正常访问方式即可
```bash
$ curl localhost:5000/api/book/10?callback=foo
```
```bash
foo({"data": {"id": 10, "name": "wxnacy"}, "meta": {"Content-Type": "application/javascript", "status": 200}})
```


## 参考
- [Flask-Restless](https://flask-restless.readthedocs.io/en/stable/)
- [Request preprocessors and postprocessors](https://flask-restless.readthedocs.io/en/stable/customizing.html#request-preprocessors-and-postprocessors)
- [Request preprocessors and postprocessors](https://flask-restless.readthedocs.io/en/latest/processors.html)
