---
title: Shell 获取字符串长度的几种方式
date: 2020-01-07 17:43:52
tags: [shell]
---

记录几种获取字符串长度的方式

<!-- more -->
<!-- toc -->

```bash
$ str=wxnacy
```

```bash
$ echo ${#str}
```

```bash
# -n 是去掉 \n 符号，不然计算的长度为 7
$ echo $(echo -n $str | wc -c)
```

```bash
$ echo $str | awk '{print length($0)}'
```
