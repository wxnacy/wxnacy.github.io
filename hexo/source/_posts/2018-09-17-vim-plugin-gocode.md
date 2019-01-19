---
title: Vim 插件 gocode：Go 代码补全
tags:
  - vim
  - go
date: 2018-09-17 18:12:42
---


[专辑：Vim 练级手册](/vim)

[gocode](https://github.com/nsf/gocode) 可以在 Vim 中实现 Go 语言的代码补全提示。

<!-- more --><!-- toc -->

## 预览
![vim-gocode.gif](/images/vim-gocode.gif)

## 安装

安装方式很简单

**下载源码**

```bash
$ go get -u github.com/nsf/gocode
```

**执行脚本**

进入根目录 `${GOPATH}/src/github.com/nsf/gocode`

如果你使用 pathogen 管理项目可以执行

```bash
$ ./pathogen_update.sh
```

除此之外可以选择执行下面两个中任意一个

**软连接**

```bash
$ ./symlink.sh
```

**直接复制**

```bash
$ ./update.sh
```

gocode 的安装工作已经完成了，但是这时如果你的环境还是不工作，那么可能因为没有安装 YouCompleteMe，我的测试是需要基于它才能工作的，这部分的安装可以看我的文章[Vim 插件 YouCompleteMe 代码自动补全](/2017/09/22/vim-plugin-youcompleteme/)
