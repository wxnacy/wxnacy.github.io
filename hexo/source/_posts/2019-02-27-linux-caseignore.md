---
title: Linux Tab 命令提示时忽略大小写
date: 2019-02-27 09:56:39
tags: [linux]
---

Linux 环境如何不装 `zsh` 等更加智能的 bash 工具，通常在 Tab 键提示命令时都会区分大小写，这样很不方便，我们可以做点简单修改让它忽略大小写。

<!-- more --><!-- toc -->

默认情况下 `~` 目录下是没有 `.inputrc` 文件的，手动创建并赋值

```bash
$ echo 'set completion-ignore-case on' >> .inputrc
```

然后退出终端，重新进入，这时命令行已经忽略大小写了。
