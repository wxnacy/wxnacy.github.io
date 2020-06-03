---
title: Mac 电脑显示隐藏文件
tags:
  - mac
date: 2020-06-03 09:49:19
---


Mac 电脑显示隐藏文件的两种方式。

<!-- more -->
<!-- toc -->

## 快捷键

`command + shift + .` 快捷键可以控制隐藏文件的显示与否，非常方便

## 命令行

作为程序员当然还要了解命令行的方式

```bash
# 显示隐藏文件
$ defaults write com.apple.finder AppleShowAllFiles yes
# 不显示隐藏文件
$ defaults write com.apple.finder AppleShowAllFiles no
```

然后再重启下 Finder

```bash
$ killall Finder /System/Library/CoreServices/Finder.app
```
