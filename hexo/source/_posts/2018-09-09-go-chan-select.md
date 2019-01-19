---
title: Go 使用 chan + select 实现简单的多进程任务
date: 2018-09-09 16:08:23
tags: [go]
---

在 Go 中使用 go 来执行一个函数即可生成一个线程，比如

<!-- more --><!-- toc -->

```go
package main

import (
    "fmt"
)

func PrintNum(a int) {
    fmt.Println(a)
}

func main() {
    go PrintNum(1)
    go PrintNum(2)

    fmt.Println("Done")
}
```

运行结果可能为

```bash
1
Done
```

`2` 并没有被打印，因为主线程不会去等待子线程执行完才结束，能执行多少就多少，所以 `PrintNum(2)` 就可能没有被执行。

这种情况我们需要让主线程等待一下子线程，比如一秒钟

```go
package main

import (
    "fmt"
    "time"
)

func PrintNum(a int) {
    fmt.Println(a)
}

func main() {
    go PrintNum(1)
    go PrintNum(2)

    time.Sleep(1 * time.Second)
    fmt.Println("Done")
}
```

```bash
1
2
Done
```

这次正常运行结果。

不过实际开发中，子线程的个数和所需要的时间一定是不确定的，我们不可能去指定一个固定时间来等待子线程，比如

```go
for i := 0; i < 10; i++ {
    go func() {
        time.Sleep(1 * time.Second)
        PrintNum(i)
    }()
}
```

这时候我们需要使用 select 来进行判断，像这样

```go
t := time.NewTicker(200 * time.Millisecond)
defer t.Stop()

Loop:
for true{
    select {
        case <-t.C: {
            fmt.Println("inprogress")
        }
        case <- c: {
            fmt.Println("Done")
            break Loop
        }
    }
}
```

将 select 嵌套在死循环中，通过管道来判断子线程的任务是否执行完毕，如果 c 管道没有值，那么将一直进行 `t.C` 的操作

然后在认定子线程完成时，给管道 c 传入值

```go
c := make(chan int, 1)
if i = 4 {
    c <- 1
}
```

完整代码见[github](https://github.com/wxnacy/study/blob/master/goland/src/multithread/chan_select.go)

运行结果如下

```bash
0
1
2
3
4
Done
```
