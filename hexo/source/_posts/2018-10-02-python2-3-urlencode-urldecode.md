---
title: Python2 和 Python3 处理 urlencode 和 urldecode 的区别
date: 2018-10-02 13:58:56
tags: [python]
---

Python2 和 Python3 对于处理 urlencode 有些区别

<!-- more --><!-- toc -->

## Python2

```python
>>> import urllib
>>> f = { 'eventName' : 'myEvent', 'eventDescription' : '中国'}
>>> urllib.urlencode(f)
'eventName=myEvent&eventDescription=%E4%B8%AD%E5%9B%BD'
>>> urllib.quote("中国 北京")
'%E4%B8%AD%E5%9B%BD%20%E5%8C%97%E4%BA%AC'
>>> urllib.unquote('%E4%B8%AD%E5%9B%BD%20%E5%8C%97%E4%BA%AC')
'\xe4\xb8\xad\xe5\x9b\xbd \xe5\x8c\x97\xe4\xba\xac'
# 需要手动转为 unicode
>>> urllib.unquote('%E4%B8%AD%E5%9B%BD%20%E5%8C%97%E4%BA%AC').decode('utf8')
u'\u4e2d\u56fd \u5317\u4eac'
```

## Python3

```python
>>> from urllib.parse import urlencode
>>> f = { 'eventName' : 'myEvent', 'eventDescription' : '中国'}
>>> urlencode(f)
'eventName=myEvent&eventDescription=%E4%B8%AD%E5%9B%BD'
>>> from urllib.parse import quote
>>> quote("中国")
'%E4%B8%AD%E5%9B%BD'
>>> from urllib.parse import unquote
>>> unquote('%E4%B8%AD%E5%9B%BD')
'中国'
```

对字符串的转码上除了 `quote` 还有 `quote_plus` 方法，他们的区别在于，前者会把空格转为 `%20`，后者转为 `+`

- [quote_plus](https://docs.python.org/2/library/urllib.html#urllib.quote_plus)
