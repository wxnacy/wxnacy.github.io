---
title: Go 语法错误：Non-declaration statement outside function body
tags:
  - go
date: 2018-08-16 15:25:50
---


编程语言都是相通的，但也很多意想不到的不同，比如今天就碰见一个语法错误。

<!-- more --><!-- toc -->
运行如下代码会报错误

```go
package main

import (
    "fmt"
)

b := 1

func main() {
    fmt.Println(b)
}
```

```bash
syntax error: non-declaration statement outside function body
```

原因在于 `:=` 只能用于方法内，当定义全局变量时只能通过 `var` 关键字来定义

```go
package main

import (
    "fmt"
)

var b = 1

func main() {
    fmt.Println(b)
}
```

- [Non-declaration statement outside function body in Go](https://stackoverflow.com/questions/20508356/non-declaration-statement-outside-function-body-in-go)
