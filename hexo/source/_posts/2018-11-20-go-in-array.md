---
title: Go 判断数组中是否包含某个 item
date: 2018-11-20 17:50:48
tags: [go]
---

Go 中不像 Python 那样可以通过 `a in []` 判断数组是否包含某个 item，项目中只能自己编写该方法。

<!-- more -->
<!-- toc -->

刚入门时第一个想到的方法就是对某个类型的数组进行遍历，再逐个对比，但这样有个最大的问题就是我们只能对一种类型的数组进行对比，不能灵活的应对各种类型。

## reflect

在 stackexchange 中看到一个方法，充分的利用了 `reflect` 包对 `interface{}` 进行判断，如下

```go
package main

import "reflect"

func Contains(array interface{}, val interface{}) (index int) {
    index = -1
    switch reflect.TypeOf(array).Kind() {
        case reflect.Slice: {
            s := reflect.ValueOf(array)
            for i := 0; i < s.Len(); i++ {
                if reflect.DeepEqual(val, s.Index(i).Interface()) {
                    index = i
                    return
                }
            }
        }
    }
    return
}

```

## 一次遍历

**2019-03-21 更新：**

今天才从网上看到一个说法，Go 中 `reflect` 很慢，尽量不要使用，我心里咯噔一下，赶紧来测试下

对比下强类型遍历的方法

```go
func StringsContains(array []string, val string) (index int) {
    index = -1
    for i := 0; i < len(array); i++ {
        if array[i] == val {
            index = i
            return
        }
    }
    return
}
```

使用 `testing` 包来测试性能

```go
import "testing"

func BenchmarkContains(b *testing.B) {
    sa := []string{"q", "w", "e", "r", "t"}
    b.ResetTimer()
    for n := 0; n < b.N; n++ {
        Contains(sa, "r")
    }
}

func BenchmarkStringsContains(b *testing.B) {
    sa := []string{"q", "w", "e", "r", "t"}
    b.ResetTimer()
    for n := 0; n < b.N; n++ {
        StringsContains(sa, "r")
    }
}

```

运行

```bash
$ go test -bench=.

goos: darwin
goarch: amd64
pkg: github.com/wxnacy/wgo/arrays
BenchmarkContains-8              2000000               635 ns/op
BenchmarkStringsContains-8      100000000               20.3 ns/op
PASS
ok      github.com/wxnacy/wgo/arrays    4.027s
```

结果非常明显，`Contains` 方法平均每次 `635 ns`，`StringsContains` 方法平均每次 `20.3 ns`

嗯，我得先缓一下，为什么 `reflect` 这么慢呢，[reflect为什么慢](http://legendtkl.com/2016/08/06/reflect-inside/)这篇文章给了很好的解释，总结下来有两点

- 涉及到内存分配以后GC
- reflect实现里面有大量的枚举

不管怎样，`reflect` 耗时长是不争的事实，又浏览了下其他的文章，大多观点都视它如“猛虎”，避之不及。

但是静下心来想想，大可不必。慢，也是相对的。毕竟这个例子很简单，为了追求性能，当然可以使用强类型比较，那如果是更复杂的映射操作呢，Go 是强类型语言啊，你不用 `reflect` 用啥。反射就不能用，你让 SpringMVC 咋办。

## wgo

在官方完美解决这个问题前，我们只能在项目中自己写方法，或者使用第三方包 [wgo](https://github.com/wxnacy/wgo)

wgo 是类似 Python 交互命令的脚本化运行工具。

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/wgo1.gif)

该包本身包含一些开发中常用但是 Go 不具备的方法和工具。

**安装**

```bash
$ go get -u github.com/wxnacy/wgo
```

**导入**

```go
import "github.com/wxnacy/wgo/arrays"
```

**常用 Contains 方法**

```go
// Contains Returns the index position of the val in array
func Contains(array interface{}, val interface{}) (index int)
```

```go
// ContainsString Returns the index position of the string val in array
func ContainsString(array []string, val string) (index int)
```

```go
// ContainsInt Returns the index position of the int64 val in array
func ContainsInt(array []int64, val int64) (index int)
```

```go
// ContainsFloat Returns the index position of the float64 val in array
func ContainsFloat(array []float64, val float64) (index int)
```

```go
// ContainsBool Returns the index position of the bool val in array
func ContainsBool(array []bool, val bool) (index int)
```

**demo**

```go
package main

import (
    "fmt"
    "github.com/wxnacy/wgo/arrays"
)

func main() {
    var arr = []int64{1, 3, 4, 8, 12, 4, 9}
    var i int
    i = arrays.ContainsInt(arr, 8)
    fmt.Println(i)      // 3

    i = arrays.Contains(arr, int64(12))
    fmt.Println(i)      // 4
}
```


- [in_array() in Go](https://codereview.stackexchange.com/questions/60074/in-array-in-go)
