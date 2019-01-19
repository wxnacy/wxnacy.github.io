---
title: Go 如何实现不换行进度条
date: 2018-10-24 10:01:48
tags: [go]
---

在 Go 中实现不换行进度条，可以通过几行原理代码实现。

<!-- more --><!-- toc -->
```go
fmt.Printf("%s \033[K\n", "--")     // 输出一行结果
fmt.Printf("\033[%dA\033[K", 1)     // 将光标向上移动一行
fmt.Printf("%s \033[K\n", "=-")     // 输出第二行结果
```

如此往复即可实现不换行进度条

完整代码见 [single.go](https://github.com/wxnacy/study/blob/master/goland/src/progress/single.go)

输出屏幕带有屏幕的原理可见 [Go 如何给屏幕打印信息加上颜色](/2018/09/07/go-fmt-color/)

带颜色的进度条完整代码见 [color.go](https://github.com/wxnacy/study/blob/master/goland/src/progress/color.go)

如果同时有多个进度条同时运行，那原理在于将最上边的进度条使用 `fmt.Printf("\033[%dA\033[K", n)` 上移一定的行数，其余进度条顺序打印即可。

多个进度条完整代码见 [multi.go](https://github.com/wxnacy/study/blob/master/goland/src/progress/multi.go)
