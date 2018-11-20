---
title: Go 判断数组中是否包含某个 item
date: 2018-11-20 17:50:48
tags: [go]
---

Go 中不像 Python 那样可以通过 `a in []` 判断数组是否包含某个 item，项目中只能自己编写该方法。
<!-- more --><!-- toc -->
刚入门时第一个想到的方法就是对某个类型的数组进行遍历，再逐个对比，但这样有个最大的问题就是我们只能对一种类型的数组进行对比，不能灵活的应对各种类型。

在 stackexchange 中看到一个方法，充分的利用了 `reflect` 包对 `interface{}` 进行判断，如下

```go
package main

import "fmt"
import "reflect"

func in_array(val interface{}, array interface{}) (exists bool, index int) {
    exists = false
    index = -1

    switch reflect.TypeOf(array).Kind() {
    case reflect.Slice:
        s := reflect.ValueOf(array)

        for i := 0; i < s.Len(); i++ {
            if reflect.DeepEqual(val, s.Index(i).Interface()) == true {
                index = i
                exists = true
                return
            }
        }
    }

    return
}
```

- [in_array() in Go](https://codereview.stackexchange.com/questions/60074/in-array-in-go)
