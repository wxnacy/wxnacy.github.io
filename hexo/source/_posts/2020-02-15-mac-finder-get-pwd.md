---
title: Mac 电脑通过 Finder 获取文件夹的命令行地址
date: 2020-02-15 00:08:05
tags: [mac]
---

记录几种 Mac 电脑通过 Finder 获取文件地址的方式。

<!-- more -->
<!-- toc -->

## 直接复制

在文件列表中直接使用 `command + c` 复制，然后在 `Terminal` 中粘贴即可

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/finder1.png)

在 Finder 左侧的目录则需要使用 `option + command + c` 来进行复制

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/finder2.png)

## 顶部永久显示

打开 `Terminal` 并输入命令

```bash
$ defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
```

效果如图

![3](https://raw.githubusercontent.com/wxnacy/image/master/blog/finder3.png)

## 直接在终端中打开

如果你安装了 `iTerm2`，则可以通过 `右键 -》服务 -》New iTerm2 Window Here` 直接打开当前目录

![4](https://raw.githubusercontent.com/wxnacy/image/master/blog/finder4_552.png)

如果没有安装，也可以在文件夹的右键在默认终端中直接打开

![5](https://raw.githubusercontent.com/wxnacy/image/master/blog/finder5_612.png)
