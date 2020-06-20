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

<script src="https://code.jquery.com/jquery-2.0.0.js"></script>
{% asset_jupyter /Users/wxnacy/.pyenv/shims/python ../../notebook/faker/quickstart.ipynb %}


Faker 有远不止以上的用法，使用 `dir(fake)` 可以查看更多的用法

## 设置语言

Faker 默认使用英文，当然也可以设置想要的语言

<script src="https://code.jquery.com/jquery-2.0.0.js"></script>
{% asset_jupyter /Users/wxnacy/.pyenv/shims/python ../../notebook/faker/locales.ipynb %}

更多语言支持查看[文档](https://faker.readthedocs.io/en/master/locales.html)

## 命令模式

Faker 也可以在命令行中使用

<script src="https://code.jquery.com/jquery-2.0.0.js"></script>
{% asset_jupyter /Users/wxnacy/.pyenv/shims/python ../../notebook/faker/command.ipynb %}

更多使用方式查看[文档](https://github.com/joke2k/faker#command-line-usage)
