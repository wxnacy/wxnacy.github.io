---
title: Python SQLAlchemy 数据库 ORM 框架
tags:
  - python
date: 2018-01-24 21:06:15
---

[SQLAlchemy](https://www.sqlalchemy.org/) 是 Python 操作数据库的 ORM 框架。可以很方便的执行常用数据库操作，以及复杂的 SQL 语句。

<!-- more --><!-- toc -->
## 下载
```bash
$ pip install SQLAlchemy
```
查看版本
```python
>>> import sqlalchemy
>>> sqlalchemy.__version__
1.2.0
```
## 使用
### 创建表
首先我们来看一个通过映射创建表的实例
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(132))

    def __str__(self):
        return f"Book[id:{self.id}, name:{self.name}]"

Base.metadata.create_all(engine)
```
如果你复制上面的代码来执行，应该能得到下面的结果
```bash
2018-01-24 16:44:04,066 INFO sqlalchemy.engine.base.Engine
CREATE TABLE book (
        id INTEGER NOT NULL AUTO_INCREMENT,
                name VARCHAR(132),
                        PRIMARY KEY (id)

        )
2018-01-24 16:44:04,066 INFO sqlalchemy.engine.base.Engine {}
2018-01-24 16:44:04,099 INFO sqlalchemy.engine.base.Engine COMMIT
```
从日志看很明显执行了创建表的语句，我们具体来看看它都做了些什么

首先需要创建引擎，通过 `create_engine` 方法完成，`echo` 参数控制了是否输出相关日志，默认 `False`
```python
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wxnacy@127.0.0.1:3306/study?charset=utf8mb4'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
```
接下来需要创建一个映射用的基类 `Base`，所有需要映射表的类都要继承这个类，才能完成相关库的操作，比如 `Book`，在 `Book` 中设置参数 `__tablename__` 代表映射的表名，各个字段需要通过 `Column` 方法来赋值，并设置相应的字段类型
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(132))

    def __str__(self):
        return f"Book[id:{self.id}, name:{self.name}]"
```
最后通过基类对所给引擎的子类进行映射创建
```python
Base.metadata.create_all(engine)
```
### 操作数据
下面我们正式操作数据，下面是个增删改查的例子
```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

book = Book(name="new book")
session.add(book)
session.commit()
print(book)         # > Book[id:1, name:new book]   查询数据

book = session.query(Book).filter_by(id=1).first()
print(book)         # > Book[id:1, name:new book]   通过id查询

book.name = "wxnacy"
session.add(book)
session.commit()

print(book)         # > Book[id:1, name:wxnacy]   修改数据
session.delete(book)
session.commit()    # 删除
```
SQLAlchemy 在操作数据库时需要用到 `Session`，通过 `sessionmaker` 方法获取，操作过程中最关键的一步就是 `commit`，不然是不会同步到库中的
### 更多查询操作
`filter_by(), filter()` 两个方法提供了很完成的查询操作，可以满足平常大多数查询操作，后者的功能更强大一些
```python
# 获取满足条件的第一条数据
filter_by(name='wxnacy').first()
filter(Book.name=='wxnacy').first()     # filter 的用法稍有不同

# 获取满足条件的所有数据
filter_by(name='wxnacy').all()

# 获取满足条件的所有数据的数量
filter_by(name='wxnacy').count()

# 后续实例省去 all(), first(), count() 等

# and 操作
# 我们在 Book 中增加一个 price 价格字段
# where id = 1 and name = 'wxnacy'
filter_by(name='wxnacy', price=12)
filter_by(name='wxnacy').filter_by(price=12)
# only filter
from sqlalchemy import and_
filter(and_(Book.name='wxnacy', Book.price=12))

# in (only filter)
# where id in (1, 2)
filter(Book.id.in_([1, 2]))

# like (only filter)
# where name like '%wxn%'
filter(Book.name.like('%wxn%'))

# not equals (only filter)
# where id != 1
filter(Book.id != 1)

# not in (only filter)
# where id not in (1, 2)
filter(~Book.id.in_([1, 2]))

# or (only filter)
# where id = 1 or name = 'wxnacy'
from sqlalchemy import or_
filter(or_(Book.id == 1, Book.name == 'wxnacy'))

# order
# order by id
filter_by().order_by(Book.id)
# order by id desc
from sqlalchemy import desc
filter_by().order_by(desc(Book.id))
filter_by().order_by(Book.id.desc())
filter_by().order_by('id desc')

# limit
# limit 4
filter_by().limit(4)
```
### order by
排序有三种方式，默认为正序排列
```python
# select * from book order by id
session.query(Book).order_by(Book.id).all()

# select * from book order by id desc
from sqlalchemy import desc
session.query(Book).order_by(desc(Book.id)).all()
session.query(Book).order_by(Book.id.desc()).all()
session.query(Book).order_by('id desc').all()

```
### group by
```python
# select name, count(name) as c from book group by name
from sqlalchemy import func
session.query(Book.name, func.count(Book.name).label('c')).group_by(Book.name).all()
```
### 批量插入
```python
# insert into book (name) values ('wxnacy');
# insert into book (name) values ('wxnacy');
# 1
session.add(Book(name="wxnacy"))
session.add(Book(name="wxnacy"))
session.commit()

# 2
session.add_all([Book(name="wxnacy"), Book(name="wxnacy")])
session.commit()

# insert into book (name) values ('wxnacy'), ('wxnacy');
# 3
items = [dict(name="wxnacy"), dict(name="wxnacy")]
session.execute(Book.__table__.insert(), items)
session.commit()
```
从结果上三种方法都可以实现批量插入的效果，但是从他们生成的 SQL 语句看，前两个种就是重复执行了单条 `insert` 语句，第三种则是将批量添加的数据整合到一条语句中，从效率上讲肯定是推荐第三种方式

### 使用 SQL 语句
ORM 虽然操作方便，但是很多复杂的情况都是不能应对的，或者说我们懒得去学习那么复杂的操作，直接用 SQL 多方便啊，对吧。SQLAlchemy 也是可以直接使用 SQL 的，并且会很方便，先看一个例子吧

```python
from sqlalchemy import text

sql = "insert into book (name) values (:name)"
engine.execute(text(sql), **dict(name='use_sql'))

sql = "select * from book where name = :name"
res = engine.execute(text(sql), **dict(name='use_sql')).fetchall()
print(res)      # >  [(2, 'new book')]
```
想要执行完整 SQL 时，需要直接使用 `engine` 对象，SQL 语句需要注意的是参数的部分， `:name` 样式来做参数占位，使用 `text()` 方法将 SQL 封装，`execute` 剩下的可变参数将 SQL 需要的参数传入，插入语句直接执行，查询语句加上 `fetchall()` 方法即可。

方便是方便，然后从上面的结果来看，在查询语句时，数据并没有字段名，在读取数据值的时候非常麻烦，以前我会使用诸如下面两种方式转成可读的状态
```python
res = session.execute(text("select * from book where id = 2"))

Record = namedtuple('Record', res.keys())
records = {Record(*r) for r in res.fetchall()}
res = [r for r in records]
print(res)  # > [Record(id=2, name='new book')]
```
```python
res = session.execute(text("select * from book where id = 2"))

def _fmt_i(k, v):
    return k ,v

def _fmt(o):
    r = list(map(_fmt_i, res.keys(), o))
    return {k: v for k, v in r}
res = [_fmt(o) for o in res.fetchall()]
print(res)  # > [{'id': 2, 'name': 'new book'}]
```
这两种方式都可以解决问题，但是我心里总觉得别扭，直到看到下面的用法

```python
from sqlalchemy import text
# where id = 2 and name = 'new book'
book = session.query(Book).filter(text("id = :id and name = :name")).params(id=2, name="new book").first()
print(book) # > Book[id:2, name=new book]
```
利用的 `session` 的 `filter()` 方法，直接传入 `text()` 包装过的 SQL，再通过 `params()` 方法传入参数，得到的结果直接用映射类 `Book` 来接受，这样的“半土半洋”的查询方式才是真正的王道。

在 FLask 框架中使用 SQLAlchemy 可以使用 `Flask_SQLAlchemy` 依赖，详情见 [Flask SQLAlchemy 框架的使用](/2018/01/25/flask-sqlalchemy/)


## 参考
- [SQLAlchemy 1.2 Documentation](http://docs.sqlalchemy.org/en/latest/intro.html#documentation-overview)
