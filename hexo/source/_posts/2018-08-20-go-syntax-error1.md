---
title: 'Go 语法错误：unexpected newline, expecting comma or }'
tags:
  - go
date: 2018-08-20 15:25:46
---


编程语言都是相通的，但也很多意想不到的不同，比如今天就碰见一个语法错误。

<!-- more --><!-- toc -->
运行如下代码会报错误

```go
package main

import (
    "fmt"
)

func main() {
    var a = []int{
        1
    }
    fmt.Println(a)
}
```

```bash
syntax error: unexpected newline, expecting comma or }
```

原因在于数组想要进行多行编写时，最后一个元素后面需要加上一个逗号，如下即可

```go
func main() {
    var a = []int{
        1,
    }
    fmt.Println(a)
}
```

- [syntax error: unexpected semicolon or newline, expecting }](https://stackoverflow.com/questions/9637483/syntax-error-unexpected-semicolon-or-newline-expecting)
