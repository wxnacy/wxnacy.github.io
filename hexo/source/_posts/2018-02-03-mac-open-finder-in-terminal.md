---
title: Mac 在 Terminal 终端中打开指定 Finder
tags:
  - mac
date: 2018-02-03 14:44:51
---


Mac 因为是类 Unix 系统，不像 Windows 那样方便打开文件夹，尤其是 `/` 目录下的一
些文件夹，在 Finder 非常难找
<!-- more -->
所幸在 Shells 中有 `open` 命令可以直接打开 Finder，打开 Terminal 输入
```bash
$ open .    # 打开当前目录
```
```bash
$ open ~    # 打开用户目录
```
```bash
$ open ~/Documents    # 打开指定文件夹
```
```bash
$ open ~/Documents/test.jpg    # 打开指定文件
```
