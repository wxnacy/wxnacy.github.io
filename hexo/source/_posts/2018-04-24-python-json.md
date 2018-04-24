---
title: Python json 模块
date: 2018-04-24 16:12:08
tags: [python]
---

Python 中使用 json 模块来处理 JSON 数据的编码和解码
<!-- more -->

导入库 `import json`

- `json.dumps`：将 Python 对象编码成 JSON 字符串
- `json.loads`：将已编码的 JSON 字符串解码为 Python 对象

## loads

**语法**

```python
json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])
```

**实例**

```python
>>> import json
>>> json.loads('["one", 42, true, null]')
['one', 42, True, None]
```

## dumps

**语法**

```python
json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
```

**实例**

```python
>>> json.dumps(['one', 42, True, None, '中国'])
'["one", 42, true, null, "\\u4e2d\\u56fd"]'
```

**禁止 ASCII 转码**

```python
>>> json.dumps(['one', 42, True, None, '中国'], ensure_ascii=False)
'["one", 42, true, null, "中国"]'
```

**格式化**

```python
>>> print(json.dumps({'a': 'wxnacy', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': ')))
{
    "a": "wxnacy",
    "b": 7
}
```

- [Python JSON](http://www.runoob.com/python/python-json.html)
