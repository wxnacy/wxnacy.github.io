---
title: Go Linux、Mac、Windows 平台交叉编译安装
tags:
  - go
date: 2018-09-14 10:26:42
---


Go 支持交叉编译，在可以一个平台上生成多个平台的执行文件。

<!-- more --><!-- toc -->

假设有一个项目结构如下

```bash
$GOPATH--/bin
      |
      |--/src/test/main.go
```

**Mac**

```bash
$ CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go install test
$ CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go install test
```

这样将会在 bin 目录下生成 `linux_amd64, windows_amd64` 两个相应的目录其中包含了各自的二进制文件

**参数**

- GOOS：目标平台的操作系统（darwin、freebsd、linux、windows）
- GOARCH：目标平台的体系架构（386、amd64、arm）
- CGO：交叉编译不支持 CGO 所以要禁用它

**Linux**

```bash
$ CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go install test
$ CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go install test
```

**Windows**

```bash
$ SET CGO_ENABLED=0 SET GOOS=darwin SET GOARCH=amd64 go install test
$ SET CGO_ENABLED=0 SET GOOS=windows SET GOARCH=amd64 go install test
```
