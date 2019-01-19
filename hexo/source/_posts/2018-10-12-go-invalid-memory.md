---
title: Go 报错 invalid memory address or nil pointer dereference
date: 2018-10-12 11:10:56
tags: [go]
---

在写 Go 程序时报了一个莫名的错误，如标题。

<!-- more --><!-- toc -->
仔细排查后发现问题出在这个块代码

```go
rows, err := db.Query(query, args...)
defer rows.Close()
if err != nil {
    return nil, err
}
```

经过 Google 后发现，`defer` 的位置不正确

> The defer only defers the function call. The field and method are accessed immediately.

修改后即可

```go
rows, err := db.Query(query, args...)
if err != nil {
    return nil, err
}
defer rows.Close()
```

- [Go: panic: runtime error: invalid memory address or nil pointer dereference](https://stackoverflow.com/questions/16280176/go-panic-runtime-error-invalid-memory-address-or-nil-pointer-dereference)
