---
title: Go 将 error 转换为 string
date: 2018-11-02 10:01:51
tags: [go]
---

在 Go 中打印 error 可以直接使用 `fmt.Println(err)`，那么如何将 error 转换为 string 呢。

<!-- more --><!-- toc -->

`toString()` ?，这个是在 java 中，Go 并没有一个统一的方法来转换 string。

`error` 有一个接口

```go
type error interface {
    Error() string
}
```

我们可以使用 `err.Error()` 方法来转换 string

- [error](https://golang.org/pkg/builtin/#error)
