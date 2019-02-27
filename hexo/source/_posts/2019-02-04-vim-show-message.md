---
title: Vim 查看环境信息
date: 2019-02-04 10:37:59
tags: [vim]
---

Vim 可以直接在命令行模式查看很多环境信息。

<!-- more --><!-- toc -->

## Vim 信息

```vim
:version            " 版本信息和加载 vimrc 顺序等信息"
:scriptnames        " 查看 script 脚本的加载顺序"
:messages           " 查看 echom 打印信息"
:function           " 查看加载的 function 列表"
:set all            " 查看 Vim 所有变量"
:set                " 查看 Vim 所有与系统不同的变量"
:set variable?      " 显示指定 Vim 变量的当前值
:set runtimepath?   " 显示 script 搜索路径
```

## 环境变量

```vim
:echo $HOME         " 用户根目录"
:echo $VIM          " Vim 程序安装目录"
:echo $VIMRUNTIME   " Vim 程序位置"
:echo $MYVIMRC      " .vimrc 文件位置"
```
