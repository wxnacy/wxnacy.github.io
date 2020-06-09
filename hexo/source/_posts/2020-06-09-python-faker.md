---
title: Python Faker 造假大师
date: 2020-06-09 22:18:35
tags: [python]
---

今天介绍一款堪称“造假大师”的 Python 模块 [Faker](https://github.com/joke2k/faker)


<!-- more -->
<!-- toc -->

李哥镇楼

![tI8JU0.gif](https://s1.ax1x.com/2020/06/09/tI8JU0.gif)

有了 Faker 再也不用手动造假了，它可以非常简单的实现你大部分的造假场景。

## 快速入门

安装

```bash
$ pip install Faker
```

使用

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

>>> from faker import Faker
>>> fake = Faker()
>>> fake.name()
'Jacob Long'
>>> fake.address()
'375 Parks Valleys Suite 232\nCynthiaview, KY 40321'
>>> fake.text()
'Prove east small son the. Reflect total clearly south. Drug enough far generation.\nBase begin read k
id number strong total.'
>>> fake.user_agent()
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.2 (KHTML, like Gecko) Chrome/46.0.879.0 Safari/536.2'
>>> fake.ipv4()
'36.77.172.61'
>>> fake.android_platform_token()
'Android 4.4.1'
>>> fake.firefox()
'Mozilla/5.0 (Android 9; Mobile; rv:42.0) Gecko/42.0 Firefox/42.0'
>>> fake.ios_platform_token()
'iPad; CPU iPad OS 9_3_5 like Mac OS X'
```

Faker 有远不止以上的用法，使用 `dir(fake)` 可以查看更多的用法

## 设置语言

Faker 默认使用英文，当然也可以设置想要的语言

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

# 设置单个语言
>>> fake = Faker('zh_CN')
>>> fake.name()
'雷峰'

# 设置多个语言
>>> fake = Faker(['zh_CN', 'ja_JP', 'en_US'])
>>> for _ in range(10):
...     fake.name()
...
'杜林'
'小林 加奈'
'Lisa Contreras'
'高橋 涼平'
'Jacob Phillips'
'Sharon Weaver'
'邓秀珍'
'若松 真綾'
'山口 零'
'易红梅'

# 设置多语言的权重

>>> from collections import OrderedDict
>>> locales = OrderedDict([
...     ('en-US', 1),
...     ('en-PH', 2),
...     ('ja_JP', 3),
... ])
>>> fake = Faker(locales)

# 获取指定的语言列表
>>> fake.locales
['en_US', 'en_PH', 'ja_JP']

# 单独获取列表中某一个语言
>>> fake['en-US'].name()
'Casey Todd'

```

更多语言支持查看[文档](https://faker.readthedocs.io/en/master/locales.html)

## 命令模式

Faker 也可以在命令行中使用

```bash
$ faker name
Brian Foster

# 设置语言
$ faker -l zh_CN name
阎艳

# 重复三次，并设置后缀
$ faker -r 3 -s ";" name
Matthew Cook;
Michael Sutton;
Meredith Krueger;
```

更多使用方式查看[文档](https://github.com/joke2k/faker#command-line-usage)
