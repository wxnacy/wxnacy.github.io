---
title: Go 结构体、数组、字典和 json 字符串的相互转换
date: 2018-08-19 15:48:33
tags: [go]
---

Go 语言中 `encoding/json` 包可以很方便的将结构体、数组、字典转换为 json 字符串。

<!-- more --><!-- toc -->

**引用**

```go
import "encoding/json"
```

**语法**

- 解析

```go
// v 传入结构体、数组等实例变量
// []byte 字节数组
// error 可能会有的错误
func Marshal(v interface{}) ([]byte, error)
```

- 反解析

```go
// []byte 字节数组
// v 传入结构体、数组等实例变量的指针地址
// error 可能会有的错误
func Unmarshal(data []byte, v interface{}) error
```

**代码**

```go
package main

// https://golang.org/pkg/encoding/json/
// https://cloud.tencent.com/developer/section/1141542#stage-100023262

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
    // 将字符串反解析为结构体
    json.Unmarshal([]byte(s), &user)
    fmt.Println(user)   // {1 wxnacy}

    var d map[string]interface{}
    // 将字符串反解析为字典
    json.Unmarshal([]byte(s), &d)
    fmt.Println(d)      // map[id:1 name:wxnacy]


    s = `[1, 2, 3, 4]`
    var a []int
    // 将字符串反解析为数组
    json.Unmarshal([]byte(s), &a)
    fmt.Println(a)      // [1 2 3 4]

    // 将结构体解析为字符串
    b, e := json.Marshal(user)
    fmt.Println(e)
    fmt.Println(string(b))  // {"id":1,"name":"wxnacy"}

    b, e = json.Marshal(a)
    fmt.Println(string(b), e)   // [1,2,3,4] <nil>

    b, e = json.Marshal(d)
    fmt.Println(string(b), e)   // {"id":1,"name":"wxnacy"} <nil>
}
```

- [Package json](https://golang.org/pkg/encoding/json/)
