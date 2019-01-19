---
title: Go 截取字符串
date: 2018-09-23 09:57:02
tags: [go]
---

学的语言多了，难免会搞混，Go 在编写习惯上跟 Java 很像，在截取 string 时习惯用了 `substring`，很显然不成功。

<!-- more --><!-- toc -->
在截取字符串和数组上 Go 跟 Python 很像，直接用索引截取即可

```go
s[0:3]
```
