---
title: Go JSON 数据格式化输出
date: 2018-11-19 11:13:00
tags: [go]
---

Go 中 `encoding/json` 包提供了格式化输出 JSON 数据的方法。

<!-- more --><!-- toc -->

```go

import "encoding/json"

var data = map[string]string{"name": "wxnacy"}

json.MarshalIndent(data, "", "    ")

```

```json
{
    "name": "wxnacy"
}
```

使用制表格来缩进可以使用

```go
json.MarshalIndent(data, "", "/t")
```
