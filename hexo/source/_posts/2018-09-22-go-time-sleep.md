---
title: Go time Sleep 实现延时
date: 2018-09-22 14:42:43
tags: [go]
---

Go 中 time.Sleep 不能传入数字来实现延时，而是传入 `time.Duration`

<!-- more --><!-- toc -->

```go
time.Sleep(time.Duration(200) * time.Millisecond)
```
```go
time.Sleep(1 * time.Second)
```

