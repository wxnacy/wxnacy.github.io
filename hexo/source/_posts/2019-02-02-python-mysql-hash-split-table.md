---
title: Python 实现 Mysql hash 分表的增删改查
date: 2019-02-02 13:59:44
tags: [python, mysql]
---

Mysql 水平分表方式中，比较适合频繁操作全部数据的方式为 hash 取模，比如用户表，所有数据都会频繁使用，使用 hash 取模的方式可以平均的将数据分配到各个表中。

<!-- more --><!-- toc -->

理解起来并不难，但是在写代码时需要讲究一些方法，如果有 10 个表，我们总不能写 10 个 Model 进行查询操作吧。

好在 Python 中可以利用 `type()` 方法动态创建 `class`，我们可以根据 id 来生成相应的 Model。

先来创建两个表

```mysql
CREATE TABLE `test_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL DEFAULT '' COMMENT '名字',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='测试';
```

```mysql
CREATE TABLE `test_0` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL DEFAULT '' COMMENT '名字',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='测试';
```

我们使用 `flask-sqlalchemy` 模块来进行 ORM 操作，正常的写法应该是

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Test(db.Model):
    __tablename__ = 'test_0'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default='')

# 插入数据

t = Test()
t.id = 1
t.name  = 'test'
db.session.add(t)
db.session.commit()

# 查询

Test.query.filter_by(id=1).first()
```

我说过我不想在写一个 `Test1` 来对应 `test_1` 表了，所以我需要对 `Test` 做一些修改

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Test():
    _model = {}

    @staticmethod
    def model(test_id):
        # 通过取余的方式将数据平均分配到两个表中
        index = test_id % 2
        tablename = 'test_{}'.format(index)
        classname = 'Test_{}'.format(index)

        Model = Test._model.get(classname)
        if not Model:
            Model = type(classname, (BaseModel, db.Model), {
                '__module__': __name__,
                '__name__': classname,
                '__tablename__': tablename,

                'id' : db.Column(db.BIGINT, primary_key=True),
                'name' : db.Column(db.String, default="", doc=""),
            })
            Test._model[classname] = Model
        return Model

# 插入数据

T = Test.model(1)
t = T()
t.id = 1
t.name = 'test'
db.session.add(t)
db.session.commit()

# 查询

T.query.filter_by(id=1).first()
```
