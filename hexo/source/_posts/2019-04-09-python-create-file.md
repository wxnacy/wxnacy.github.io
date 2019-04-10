---
title: Python 如何创建文件
tags:
  - python
date: 2019-04-09 18:02:33
---


Python 中可以使用 `open()` 内置方法来创建和打开文件。

<!-- more -->


**语法**

```bash
f = open(file, [mode])
```

Mode:
- `x` 创建文件，如果文件已经存在会报错。
- `w` 创建可写文件，写入内容覆盖文件。
- `r` 获取可读文件，默认模式。
- `a` 打开一个可追加文件，广告默认在文尾。
- `t` 打开一个 text 模式，默认模式
- `b` 打开一个二进制模式

**创建文件**

```python
>>> f = open('/tmp/test', 'x')
>>> f = open('/tmp/test', 'x')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    f = open('/tmp/test', 'x')
FileExistsError: [Errno 17] File exists: '/tmp/test'
```

**创建可写文件**

```python
>>> f = open('/tmp/test1', 'w')
>>> f.close()
>>> f = open('/tmp/test1', 'w')
>>> f.write('hw')
2
>>> f.close()
```

**创建可追加文件**

```python
>>> f = open('/tmp/test1', 'a')
>>> f.write('hw')
2
>>> f.close()
>>> f = open('/tmp/test1', 'r')
>>> f.read()
'hwhw'
```

**获取可读文件**

```python
>>> f = open('/tmp/test1', 'r')
>>> f.read()
'hwhw'
>>> f.close()
>>> f = open('/tmp/test1', 'rb')    # 以二进制打开
>>> f.read()
b'hwhw'
>>> f.close()
```

- [Python File Handling: Create, Open, Append, Read, Write](https://www.guru99.com/reading-and-writing-files-in-python.htm)
