---
title: Go 条件语句
date: 2018-08-13 14:55:12
tags: [go]
---

Go 语言中条件语句和 Java 即为相似，只是少了一对小括号。

<!-- more --><!-- toc -->

## if

```go
a := 1
if a > 0 {
    fmt.Println("> 0")
} else {
    fmt.Println("< 0")
}
```

```go
if a := 1;a > 0 {
    fmt.Println("> 0")
} else {
    fmt.Println("< 0")
}
```

## switch

switch 语句用于基于不同条件执行不同动作，每一个 case 分支都是唯一的，从上直下逐一测试，直到匹配为止。。

switch 语句执行的过程从上至下，直到找到匹配项，匹配项后面也不需要再加break


```go
a := 1
var c string

switch a {
    case 1:
        c = "1"
    case 2:
        c = "2"
    default:
        c = "default"
}
fmt.Println(c)
```

- [Go 语言条件语句](http://www.runoob.com/go/go-decision-making.html)
