---
title: Go 语法错误：main redeclared in this block
tags:
  - go
date: 2018-08-23 15:20:05
---


在同一个目录中我创建了两个文件

<!-- more --><!-- toc -->

**main.go**

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

**test.go**

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

单独运行没有问题，但是当安装该包时报错

```bash
./test.go:10:6: main redeclared in this block
```
原因在于在同一个包内不能有多个 `main` 方法，不然程序无法判断程序入口
