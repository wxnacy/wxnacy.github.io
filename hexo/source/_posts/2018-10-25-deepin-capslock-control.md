---
title: Deepin 交换 CapsLock 和 Control 键位
date: 2018-10-25 10:05:19
tags: [linux]
---

对于程序员来说，`CapsLock` 键位基本是没用的，但是它又占着一个黄金位置，将它换成 `Control` 键，在各个终端命令中作为 Leader 键是非常合适的，在 Mac 中可以直接从设置面板中修改，在 Deepin 中稍微费点事。

<!-- more --><!-- toc -->

**打开 Terminal**

使用 `ctrl + alt + t` 键快速打开一个 Terminal。

**创建配置文件**

在用户当前目录 `~` 下创建 `.xmodmap` 文件，如果有，直接编辑。

```bash
$ cd ~
$ touch .xmodmap
$ vim .xmodmap
```

将如下配置复制进文件，然后保存退出

```bash
remove Lock = Caps_Lock
remove Control = Control_L
keysym Control_L = Caps_Lock
keysym Caps_Lock = Control_L
add Lock = Caps_Lock
add Control = Control_L
```

使用文件生效

```bash
$ xmodmap .xmodmap
```

如果执行后没有报错，此时两个键位已经交换成功

**参考**

- [deepin linux下怎么交换ctrl和capslock键](https://jingyan.baidu.com/article/a24b33cd2bb8e019fe002bb6.html)
