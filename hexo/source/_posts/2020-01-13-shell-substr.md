---
title: Shell 截取字符串的几种方式
date: 2020-01-13 23:33:18
tags: [shell]
---

Shell 中截取字符串的方式也有很多种。

<!-- more -->
<!-- toc -->

```bash
$ str=https://wxnacy.com/2020/01/13/shell-substr
```

**从索引处开始截取**

```bash
$ echo ${str:6}
//wxnacy.com/2020/01/13/shell-substr
```

**截取指定长度**

```bash
$ echo ${str:6:8}
//wxnacy
```

**从右边索引处开始截取**

```bash
$ echo ${str:0-6}
substr
```
