---
title: Python chardet 判断字符编码
date: 2018-07-26 10:38:22
tags: [python]
---

在处理微信的编码时经常会很头疼，因为它的数据有时候是 `utf-8` 有时候是 `ISO-8859-1`

<!-- more --><!-- toc -->
使用 `chardet` 模块可以判断字符的编码

```python
>>> import chardet
>>> chardet.detect('哈哈'.encode())
{'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
>>> chardet.detect('哈哈'.encode('GB2312'))
{'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}
>>>
```
