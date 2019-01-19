---
title: Ubuntu 中 VIM 剪切板与系统交互
date: 2018-07-18 13:28:29
tags: [vim]
---

在 Ubuntu 服务器中使用 Vim 剪切板默认是不支持与系统交互的。

<!-- more --><!-- toc -->
你可以通过命令查询

```bash
$ vim --version | grep "clipboard"

-clipboard       +insert_expand   +path_extra      +user_commands
+emacs_tags      +mouseshape      +startuptime     +xterm_clipboard
```

`clipboard` 前边是 `-` 号，即为不支持

此时需要下载图形化界面 Vim

```bash
$ sudo apt update -y
$ sudo apt install vim-gnome -y
```

再次查看已经可以支持

**将 Vim 数据复制到剪切板**

```bash
"+y
```

**将剪切板数据复制到 Vim**

`normal` 模式下

```bash
"+p
```
