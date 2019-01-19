---
title: Go 将 rune 转换为 string
date: 2018-11-07 09:41:13
tags: [go]
---

在 Go 中有几种方式将 rune 类型转换为 string

<!-- more --><!-- toc -->

```go
string('c')
// string(rune('c'))
```

```bash
c
```

或者借助 `strconv` 包

```go
strconv.QuoteRune('c')
```

```bash
'c'
```

这种方式会将单引号也打印出来
