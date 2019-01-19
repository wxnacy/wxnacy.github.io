---
title: Go 回调函数
tags:
  - go
date: 2018-08-28 09:53:18
---


Go 与 Javascript 有一个相同的特性就是异步，异步程序回调函数是必不可少的，Go 中有两种方式实现回调。

<!-- more --><!-- toc -->

## 直接传入函数

```go
package main

import (
    "fmt"
)

func Func3(a int, call func(b int) int) int {
    return call(a)
}

func main() {

    res := Func3(1, func(b int) int {
        return b
    })
    fmt.Println(res)    // 1

}
```

## 先定义后传入

```go
package main

import (
    "fmt"
)

type Callback func(a int) int

func Func2(b int, callback Callback) int {
    return callback(b)
}

func main() {

    res := Func2(1, func(a int) int{
        return a + 2
    })
    fmt.Println(res)    // 3

}
```
