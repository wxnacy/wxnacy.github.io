---
title: Linux 管道命令（竖线）和在 Go 语言中的应用
date: 2018-09-02 13:51:46
tags: [linux, go]
---

Linux 系统中有个很有意思的命令，管道，也就是竖线（|），使用方法为

<!-- more --><!-- toc -->
```bash
$ cmd1 | cmd2
```

| 可以将 cmd1 的运行结果传递给 cmd2，这个命令非常灵活多用。

比如：

```bash
$ curl http://baidu.com | grep 'bai'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    81  100    81    0     0    131      0 --:--:-- --:--:-- --:--:--   131
<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
```

**在 Go 中的应用**

管道的内容，位于 os.Stdin 里，通过 os.Stdin 的 mode 值来判断程序是否通过管道调用，然后通过 bufio 包获取数据

```go
package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

func main() {
    fileInfo, _ := os.Stdin.Stat()
    fmt.Println(fileInfo.Mode(), os.ModeNamedPipe, os.ModeNamedPipe)
    if (fileInfo.Mode() & os.ModeNamedPipe) != os.ModeNamedPipe {
        log.Fatal("The command is intended to work with pipes.")
    }
    s := bufio.NewScanner(os.Stdin)
    for s.Scan() {
        fmt.Println(s.Text())
    }
}
```

可以对它进行封装

```go
func HasStdin() (string, bool) {
    fileInfo, _ := os.Stdin.Stat()
    if (fileInfo.Mode() & os.ModeNamedPipe) != os.ModeNamedPipe {
        return "", false
    }
    s := bufio.NewScanner(os.Stdin)
    resList := make([]string, 0, 0)
    for s.Scan() {
        resList = append(resList, s.Text())
    }
    result := strings.Join(resList, "\n")
    return result, true
}
```

完整代码见[demo](https://github.com/wxnacy/study/blob/master/goland/src/args/stdin.go)
