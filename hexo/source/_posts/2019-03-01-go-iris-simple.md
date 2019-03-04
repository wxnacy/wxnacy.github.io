---
title: Go Web 框架 iris 简单入门
tags:
  - go
date: 2019-03-01 17:22:15
---


作为后端开发，初识一门语言时，选一款合适的 Web 框架是很有必要的。

<!-- more --><!-- toc -->

经过这篇文章 [6 款最棒的 Go 语言 Web 框架简介](https://studygolang.com/articles/11897?fr=sidebar)的介绍，有理由相信 [iris](https://github.com/kataras/iris) 是目前最优秀的 Web 框架，今天简单了解下这个框架的使用。

## 下载

```bash
$ go get -u github.com/kataras/iris
```

## Hello World

```go
package main

import (
    "github.com/kataras/iris"
)

var app *iris.Application

func main() {
    app = iris.Default()
    app.Get("/hello", func(ctx iris.Context) {
        ctx.JSON(iris.Map{
            "message": "Hello World",
        })
    })
    // listen and serve on http://0.0.0.0:8080.
    app.Run(iris.Addr(":8080"))
}
```

初始化和路由配置都很简单

```bash
$ go run main.go
$ http :8080/hello

HTTP/1.1 200 OK
Content-Length: 25
Content-Type: application/json; charset=UTF-8
Date: Thu, 28 Feb 2019 07:25:00 GMT

{
    "message": "Hello World"
}
```

## 日志输出

```go
package main

import (
    "github.com/kataras/iris"
    "github.com/kataras/iris/middleware/logger"
)

var app *iris.Application

func main() {
    app = iris.Default()
    app.Use(logger.New())
    app.Logger().SetLevel("debug")
    app.Get("/hello", func(ctx iris.Context) {
        app.Logger().Debug("Hello World")
        app.Logger().Info("Hello World")
        app.Logger().Error("Hello World")
        ctx.JSON(iris.Map{
            "message": "Hello World",
        })
    })
    // listen and serve on http://0.0.0.0:8080.
    app.Run(iris.Addr(":8080"))
}
```

## template 使用

使项目目录结构如下

```bash
.
├── README.md
├── main.go
├── static
│   └── hello.js
└── templates
    └── index.html
```

注册 template 目录和匹配文件

```go
app.RegisterView(iris.HTML("./templates", ".html"))
```

初始化静态文件目录

```go
app.StaticWeb("static", "./static")
```

传递 template 变量，并显示页面

```go
app.Get("/index", func(ctx iris.Context) {
    ctx.ViewData("name", "wxnacy")
    ctx.View("index.html")
})
```

运行

```bash
$ go run main.go
$ http :8080/index

HTTP/1.1 200 OK
Content-Length: 129
Content-Type: text/html; charset=UTF-8
Date: Thu, 28 Feb 2019 07:56:57 GMT

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title></title>
</head>
<body>
  Hello wxnacy
</body>
</html>

$ http :8080/static/hello.js

HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 51
Content-Type: application/javascript; charset=UTF-8
Date: Thu, 28 Feb 2019 07:57:33 GMT
Last-Modified: Thu, Feb 28 2019 07:47:22 GMT

function hello(){
  console.log("Hello World");
};
```

完整代码地址：https://github.com/wxnacy/study/tree/master/goland/src/iris_examples/mvc-templates

## 更多的 method

```go
app.Post("/", func(ctx iris.Context){}) -> for POST http method.
app.Put("/", func(ctx iris.Context){})-> for "PUT" http method.
app.Delete("/", func(ctx iris.Context){})-> for "DELETE" http method.
app.Options("/", func(ctx iris.Context){})-> for "OPTIONS" http method.
app.Trace("/", func(ctx iris.Context){})-> for "TRACE" http method.
app.Head("/", func(ctx iris.Context){})-> for "HEAD" http method.
app.Connect("/", func(ctx iris.Context){})-> for "CONNECT" http method.
app.Patch("/", func(ctx iris.Context){})-> for "PATCH" http method.
app.Any("/", func(ctx iris.Context){}) for all http methods.
```

[更多例子](https://github.com/iris-contrib/examples)
