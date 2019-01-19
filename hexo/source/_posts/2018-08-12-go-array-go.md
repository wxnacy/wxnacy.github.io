---
title: Go 数组 array
date: 2018-08-12 17:08:45
tags: [go]
---

本章简单了解下 Go 语言的数组（array）。

<!-- more --><!-- toc -->

## 初始化

初始化固定长度的数组，并根据索引赋值

```go
var a [2]int
fmt.Println(a)      // [0 0]
a[0] = 1
fmt.Println(a)      // [1 0]
```

初始化固定长度的数组，并直接赋值

```go
a := [2]int{1, 2}
fmt.Println(a)      // [1 2]
```

初始化不确定长度的数组

```go
a := [...]int{1, 2}
fmt.Println(a)      // [1 2]

b := []int{1, 2}
fmt.Println(b)      // [1 2]
```

数组一旦确定长度，便不能更改，否则就会报错

```go
a := [2]int{1, 2}
fmt.Println(a)      // [1 2]
a = [4]int{5, 6, 7, 8}
// arrays.go|23 col 7| cannot use [4]int literal (type [4]int) as type [2]int in assignment
```

## 切片

> Go 数组的长度不可改变，在特定场景中这样的集合就不太适用，Go中提供了一种灵活，功能强悍的内置类型切片("动态数组"),与数组相比切片的长度是不固定的，可以追加元素，在追加时可能使切片的容量增大。

切片可以像 Python 一样支持 `[x:y]` 的截取方式，`x` 表示截取开始的索引数字，`y` 表示截取结束的索引数字，截取后返回一个切片

```go
h := []int{1, 2, 3, 4, 5, 6, 7}

fmt.Println(h[:])           // [1 2 3 4 5 6 7]
fmt.Println(h[0:])          // [1 2 3 4 5 6 7]
fmt.Println(h[0:len(h)])    // [1 2 3 4 5 6 7]
fmt.Println(h[2:4])         // [3 4]
fmt.Println(h[:4])          // [1 2 3 4]
```

这要比 Java 不知道简单了多少，可惜不像 Python 那样支持负数索引，不然截取尾部数据会更方便。

此时切片可以任意改变大小

```go
h = []int{1, 2, 3,4}
h = []int{1, 2, 3, 4, 5}
```

**初始化切片**

切片也可以自定义

```go
var a = make([]int, len, cap)
```

`len(), cap()` 可以获取切片的长度和长度最长可以达到多少

```go
var m = make([]int, 3, 4)
fmt.Printf("slice %v len %d cap %d", m, len(m), cap(m))
// slice [0 0 0] len 3 cap 4
```

说实话 `cap` 在使用中，并没有起到什么作用，肯定是我还了解的不够，以后明白了在更新上。


## 作为函数参数

```go
func Test(a []int) {
	fmt.Println(a)
}
a := []int{1, 2}
Test(a)     // [1 2]
```

## 方法

通过 Go 的一些内置方法可以更好的操作数组

**append**

数组长度不可更改，但是我们可以通过 `append` 方法返回一个新数组，并添加上元素。

```go
a := []int{1, 2}
a = append(a, 1)
fmt.Println(a)      // [1 2]

a = append(a, 3, 4)
fmt.Println(a)      // [1 2 3 4]
```

当 `append` 的第一个参数为切片时，可以另一个数组或切片的数据整个添加过来。

```go
a := []int{1, 2}
b := []int{3, 4}
fmt.Println(append(a[:], b...)) // [1 2 3 4]
```

**delete**

Go 中貌似是没有数组的删除方法的，不过我们可以利用 `append` 来实现这个功能。

```go
func Remove(slice []int, s int) []int {
    return append(slice[:s], slice[s+1:]...)
}

a := []int{1, 2}
a = Remove(a, 0)
fmt.Println(a)      // [2]
```

**copy**

```go
var n = []int{1, 2}
var l = make([]int, len(n), cap(n) * 2)
copy(l, n)
fmt.Println(l)  // [1 2]
```

- [Go 循环语句](/2018/08/24/go-loops/)
