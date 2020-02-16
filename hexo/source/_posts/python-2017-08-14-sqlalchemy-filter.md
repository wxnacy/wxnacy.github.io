---
title: SQLAlchemy 各种查询语句写法
date: 2017-08-14
tags: [python]
---

<!-- toc -->

## and

filter 与 filter_by 语法稍有不同

```python
User.query.filter_by(id=1,name='win').first()
User.query.filter(User.id==1,User.name == 'win').first()
```

## in
```python
sql = User.query.filter(User.id.in_([1,2]))
print(sql)

> select * from user where id in (1,2)
```

## or
```python
from sqlalchemy import or_
sql = User.query.filter(or_(User.name == 'winn',User.mobile == '183'),User.email == '371')
print(sql)

> select * from user where (name = 'winn' or mobile = '183') and email= '371'
```

## 排序

```python
from sqlalchemy import desc
User.query.order_by(create_ts).all() # 根据创建时间正序
User.query.order_by(desc(create_ts)).all() # 根据创建时间倒序
```

## 大于小于
```python
User.query.filter(User.age >= 12,User.age < 23).all()
```

## like
```python
User.query.filter(User.name.like('%win%')).all()
```

## JSON 相关

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

# select * from user where json_field -> '$.id' = 1;
User.query.filter(User.json_field['id'] == 1).all()

# select * from user where array_field -> '$[0]' = 1;
User.query.filter(User.array_field[0] == 1).all()

User.query.filter(User.array_field[].contains([1])).all()
```

