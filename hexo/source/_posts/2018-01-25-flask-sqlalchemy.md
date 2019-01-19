---
title: Flask SQLAlchemy 框架的使用
date: 2018-01-25 18:13:01
tags: [python, flask]
---

昨天介绍了 SQLAlchemy 的使用，今天介绍下在 Flask 框架中如何使用它。

<!-- more --><!-- toc -->
本章代码 Demo 地址：https://github.com/wxnacy/study/tree/master/python/flask_sqlalchemy_demo

## 下载
```bash
$ pip install Flask
$ pip install Flask_SQLAlchemy
```
`Flask_SQLAlchemy` 将 SQLAlchemy 整合到 Flask 框架中，使用起来非常方便。

## 创建 db
SQLAlchemy 需要的 `Base, engine, session` 都被整合到了一起，用 `SQLAlchemy` 类实现，该类实例需要传入 `Flask` 对象，并利用 `app.config['SQLALCHEMY_DATABASE_URI']` 来赋值 `database` 的 URI，
```python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
```
通过 db 可以获取基类 `db.Model`，Session `db.session`，引擎 `db.engine`

## 映射类
在构造映射类的时候，需要继承的基类由 `db.Model` 来实现
```python
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String, default="")

    def format(self):
        return dict(id=self.id, name=self.name)
```
## 创建 api
我们创建两个 RESTful 风格的接口，创建和查询
```python
@app.route('/book', methods=['POST'])
def create_book():
    args = request.json
    book = Book(**args)
    db.session.add(book)
    db.session.commit()
    return jsonify(book.format())

@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.filter_by(id=id).first()
    return jsonify(book.format())
```
在创建部分，与直接使用 SQLAlchemy 没有什么不同，但是在查询方面，除了可以使用 `session.query(Book)` 的方式查询，还可以使用 `Book.query` 的方式查询，这样书写会更方便。

## 运行
最后加上 `app.run()` 来启动 web 服务，运行
```bash
$ python run.py
```
启动项目

创建
```bash
$ curl -X POST localhost:5000/book -H "Content-Type:application/json" -d '{"name":"wxnacy"}'
```
```bash
{
    "id": 94,
    "name": "wxnacy"
}
```
获取
```bash
$ curl localhost:5000/book/94
```
```bash
{
    "id": 94,
    "name": "wxnacy"
}
```

## 参考
- [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
