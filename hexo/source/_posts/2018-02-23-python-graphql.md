---
title: Python 中使用 Graphql
tags:
  - python
  - graphql
date: 2018-02-23 11:14:39
---


[GraphQL](http://graphql.cn/) 既是一种用于 API 的查询语言也是一个满足你数据查询的运行时。 GraphQL 对你的 API 中的数据提供了一套易于理解的完整描述，使得客户端能够准确地获得它需要的数据，而且没有任何冗余，也让 API 更容易地随着时间推移而演进，还能用于构建强大的开发者工具。

<!-- more --><!-- toc -->
## 安装
```bash
$ pip install graphene
```

## Hello World
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        print(info)
        return 'Hello ' + name

schema = graphene.Schema(query=Query)

result = schema.execute('{ hello  }')
print(result.data)
print(result.data['hello']) # "Hello stranger"
```

## SQLAlchemy
想在项目中使用 Graphql 链接数据库是必备的，现在 Python 中链接数据库普遍使用 SQLAlchemy 框架，将两者整合起来也非常简单

安装
```bash
$ pip install "graphene-sqlalchemy>=2.0"
```
例子
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(132))

    def __str__(self):
        return f"Book[id:{self.id}, name:{self.name}]"


class BookQuery(SQLAlchemyObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    books = graphene.List(BookQuery)
    book = BookQuery

    def resolve_books(self, info):
        print(info)
        query = BookQuery.get_query(info)  # SQLAlchemy query
        return query.all()

    def resolve_book(self, info):
        query = BookQuery.get_query(info)  # SQLAlchemy query
        return query.filter(Book.id==2).first()

schema = graphene.Schema(query=Query)


query = '''
        query {
            books {
                name
            }
            book
        }
'''.strip()
result = schema.execute(query, context_value={'session': session})
print(result.data)
```

## Flask
终归我们是要在 web 接口中使用的，Graphql 也提供了 Flask 相应的框架

下载
```bash
$ pip install Flask-GraphQL
```
例子
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import Flask
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        print(info)
        return 'Hello ' + name

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
    schema=schema, graphiql=True))

app.run(port=4901)
```
在执行上述代码时，会启动一个端口 4901 的服务，访问 `http://localhost:4901/graphql` 并在左侧输入查询语句，会看到如下界面
![/images/pygraphql1.png](/images/pygraphql1.png)
这就是 Graphql 的调试页面了，在查询后，地址栏的地址会变成
```bash
http://localhost:4901/graphql?query=%7Bhello%7D
```
使用 curl 访问会直接得到 JSON 数据
```json
{"data":{"hello":"Hello stranger"}}
```
在调试到想要数据后，地址直接用到客户端即可

同时在 Flask 中直接使用 Flask-SQLAlchemy 模块会更加方便操作数据库

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene
app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


class Book(db.Model):
	__tablename__ = 'book'
	id = db.Column(db.INT, primary_key=True)
	name = db.Column(db.String, default="")
	def format(self):
		return dict(id=self.id, name=self.name)

class BookQuery(SQLAlchemyObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    books = graphene.List(BookQuery)

    def resolve_books(self, info):
        print(info)
        query = BookQuery.get_query(info)  # SQLAlchemy query
        return query.all()

schema = graphene.Schema(query=Query)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
    schema=schema, graphiql=True))

app.run(port=4901)
```

- [graphene](https://github.com/graphql-python/graphene)
- [Graphene-SQLAlchemy](https://github.com/graphql-python/graphene-sqlalchemy/)
- [flask-graphql](https://github.com/graphql-python/flask-graphql)
- [查询和变更](http://graphql.cn/learn/queries/)
