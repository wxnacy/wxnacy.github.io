---
title: Go 自动打开系统默认浏览器
tags:
  - go
date: 2019-03-04 13:48:03
---


因为 Go 可以编译 `Windows` `Darwin` `Linux` 三个平台的二进制文件，如果编写一个 Web 项目，启动后可以自动打开浏览器，那就非常方便了。

<!-- more --><!-- toc -->

首先看下三个平台打开浏览器的命令

**Darwin**

```bash
$ open http://baidu.com
```

**Windows**

```bash
$ start http://baidu.com
```

**Linux**

```bash
$ xdg-open http://baidu.com
```

接下来需要 Go 能区分平台，这里需要 `runtime` 包。

```bash
import "runtime"
platform := runtime.GOOS
// darwin windows linux
```

好接下来就可以写代码了

```go
package main
// 打开系统默认浏览器

import (
    "fmt"
    "os/exec"
    "runtime"
)

var commands = map[string]string{
    "windows": "start",
    "darwin":  "open",
    "linux":   "xdg-open",
}

func Open(uri string) error {
    run, ok := commands[runtime.GOOS]
    if !ok {
        return fmt.Errorf("don't know how to open things on %s platform", runtime.GOOS)
    }

    cmd := exec.Command(run, uri)
    return cmd.Start()
}

func main() {
    Open("http://baidu.com")
}
```
