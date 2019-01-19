---
title: Go 大小写和访问权限
tags:
  - go
date: 2018-08-21 15:04:37
---


在 Go 语言中，变量名，方法名都应该遵循驼峰命名法，不能出现下划线。这不是约定俗成，而是必须，因为这个访问权限息息相关。

<!-- more --><!-- toc -->

变量名首字母的大小写很重要，大写 `Name` 可以被外部访问，小写 `name` 不可被外部访问，即 **大写为公有变量，小写为私有变量**

这是在结构体向 json 结构解析时发现的问题

```go
package main

import (
    "fmt"
    "encoding/json"
)

type User struct {
    Id int `json:"id"`
    Name string `json:"name"`
}

func main() {
    // 字符串解析为结构体
    s := `{"id": 1, "name": "wxnacy"}`

    var user User
    json.Unmarshal([]byte(s), &user)
    fmt.Println(user)   // {1 wxnacy}
}
```

如果 `Id` 和 `Name` 变为小写，那 json 将无法将数据反解析 `User` 结构体。

