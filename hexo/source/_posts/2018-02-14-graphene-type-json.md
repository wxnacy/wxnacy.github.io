---
title: Python 中使用 Graphql 返回 JSON 类型
tags:
  - graphql
  - python
date: 2018-02-14 19:34:16
---


在使用 Graphql 在 Python 中的模块 Graphene 时，发现默认返回类型没有 JSON 格式，通过网上资料发现需要自己补充该类型才可以。

<!-- more --><!-- toc -->
## py2
```python
import graphene
from graphene.types.scalars import MIN_INT, MAX_INT
from graphql.language.ast import BooleanValue, StringValue, IntValue, ListValue, ObjectValue, FloatValue


class JSON(graphene.Scalar):
	"""
	The `JSON` scalar type represents JSON values as specified by
	[ECMA-404](http://www.ecma-international.org/
	publications/files/ECMA-ST/ECMA-404.pdf).
	"""

	@staticmethod
	def identity(value):
		if isinstance(value, (unicode, str, bool, int, float)):
			return value.__class__(value)
		elif isinstance(value, (list, dict)):
			return value
		else:
			return None

	serialize = identity
	parse_value = identity

	@staticmethod
	def parse_literal(ast):
		if isinstance(ast, (StringValue, BooleanValue)):
			return ast.value
		elif isinstance(ast, IntValue):
			num = int(ast.value)
			if MIN_INT <= num <= MAX_INT:
				return num
		elif isinstance(ast, FloatValue):
			return float(ast.value)
		elif isinstance(ast, ListValue):
			return [JSON.parse_literal(value) for value in ast.values]
		elif isinstance(ast, ObjectValue):
			return {field.name.value: JSON.parse_literal(field.value) for field in ast.fields}
		else:
			return None
```

## py3
```python
import graphene
from graphql.language.ast import BooleanValue, StringValue, IntValue, ListValue, ObjectValue, FloatValue

class JSON(graphene.Scalar):
	"""
	The `JSON` scalar type represents JSON values as specified by
	[ECMA-404](http://www.ecma-international.org/
	publications/files/ECMA-ST/ECMA-404.pdf).
	"""

	@staticmethod
	def identity(value):
		if isinstance(value, (str, bool, int, float)):
			return value.__class__(value)
		elif isinstance(value, (list, dict)):
			return value
		else:
			return None

	serialize = identity
	parse_value = identity

	@staticmethod
	def parse_literal(ast):
		if isinstance(ast, (StringValue, BooleanValue)):
			return ast.value
		elif isinstance(ast, IntValue):
			return int(ast.value)
		elif isinstance(ast, FloatValue):
			return float(ast.value)
		elif isinstance(ast, ListValue):
			return [JSON.parse_literal(value) for value in ast.values]
		elif isinstance(ast, ObjectValue):
			return {field.name.value: JSON.parse_literal(field.value) for field in ast.fields}
		else:
			return None
```

## 使用
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import graphene

class Query(graphene.ObjectType):
    test = graphene.Field(JSON)

    def resolve_test(self, info):
        return dict(name="wxnacy", age=12, types = ['shuaiqi', 'youcai'],
            book=dict(name='wohenshuai'))

schema = graphene.Schema(query=Query)

result = schema.execute('{ test  }')
print(result.data['test'])
# {'name': 'wxnacy', 'age': 12, 'types': ['shuaiqi', 'youcai'], 'book': {'name': 'wohenshuai'}}
```
完整 demo 地址：https://github.com/wxnacy/study/blob/master/python/graphql_demo/type_json.py

- [Implement JSON type](https://github.com/graphql-python/graphene/issues/384)
