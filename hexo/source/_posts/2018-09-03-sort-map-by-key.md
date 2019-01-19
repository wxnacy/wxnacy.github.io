---
title: Go 将 map 按 key 排序
date: 2018-09-03 17:24:33
tags: [go]
---

Go 在给 map 进行 key 排序时，需要做一下转换。

<!-- more --><!-- toc -->


```go
import "sort"

func main(){
    m := map[string]string{"id": "1", "name": "wxnacy"}
    keys := make([]string, 0, len(m))
    for k, _ := range m {
        keys = append(keys, k)
    }
    sort.Strings(keys)
}
```
