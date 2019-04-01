---
title: SQLAlchemy 升级报错：Can't resolve label reference for ORDER BY / GROUP BY ...
tags:
  - python
  - sqlalchemy
date: 2019-03-30 17:53:36
---


前段时间因为要使用 `insert ... on duplicate key update ..` 语句的功能，SQLAlchemy 从 1.1.5 升级到了 1.3.1，结果程序报了错

<!-- more -->

```bash
Can't resolve label reference for ORDER BY / GROUP BY. Textual SQL expression 'rank desc' should be explicitly declared as text('rank desc')
```

其实一看到这个错误，我就知道是怎么回事了，因为之前的版本其实报过警告，只是当时没有在意

```bash
SAWarning: Can't resolve label reference 'rank desc'; converting to text() (this warning may be suppressed after 10 occurrences)
```

它的意思是在未来的版本 `order_by('rank desc')` 写法将不再支持。

那换个写法就好了。

我们先来回顾下，老版本 `ORDER BY` 的几种写法，原始 SQL 如下：

```mysql
> select * from user order by id desc;
```

SQLAlchemy 的写法有三种

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

# 第一种最简单
db.session.query(User).order_by('id desc').all()

# 第二种比较符合 SQLAlchemy 语法
db.session.query(User).order_by(User.id.desc()).all()

# 第三种最麻烦
from sqlalchemy import desc
db.session.query(User).order_by(desc(User.id)).all()
```

既然新版本第一种方式不让用了，那就用第二种好了，OK，正常情况下没有，但是我修改后报了如下错。

```bash
AttributeError: type object 'VisitorLog' has no attribute 'rank'
```

找不到属性？我回看了下代码发现了问题。

原始 SQL 如下：

```mysql
> select url, count(url) as rank from visit_log group by url order by rank desc;
```

老版本 SQLAlchemy 写法

```python
from sqlalchemy import func
cls = VisitLog
res = db.session.query(
    cls.url, func.count(cls.url).label('rank')
).group_by(cls.url).order_by('rank desc').all()
```

新版本理论写法

```python
from sqlalchemy import func
cls = VisitLog
res = db.session.query(
    cls.url, func.count(cls.url).label('rank')
).group_by(cls.url).order_by(cls.rank.desc).all()
```

因为 `rank` 我是用了 `label` 方法模拟了 `as` 功能，所以报错找不到属性也是可以理解的，那这里我们需要将 `label` 单提出一个变量了，在进行 `desc()` 方法

```python
from sqlalchemy import func
cls = VisitLog
rank = func.count(cls.url).label('rank')
res = db.session.query(
    cls.url, rank
).group_by(cls.url).order_by(rank.desc).all()
```

在执行，完美解决

这套逻辑同样适用于 `GROUP BY` 语法

- [官方文档](https://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.desc)
- [python-sqlalchemy-label-usage](https://stackoverflow.com/questions/15555920/python-sqlalchemy-label-usage)
