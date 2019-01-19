---
title: Git 修改默认编辑器
date: 2018-09-30 10:31:01
tags: [git]
---

最近升级了 MacOS 新系统到 10.14.2 版本，新系统还真不是盖的，上来就好多不兼容的地方，比如 Vim。

<!-- more --><!-- toc -->
正常开发本来并没有问题，但是在处理 `git merge` 时，它调用默认编辑器 Vim 就会报错。

```bash
Vim: Caught deadly signal SEGV
```

从网上查询说是 ycm 插件导致的，需要在新系统下重新编译安装一遍才行。不过既然正常开发并没有收到影响，我何必多此一举呢，想着让 Git 不调用这个插件就得了。

```bash
$ vim -u NONE
```

该命令可以在不使用任何插件的情况下打开 Vim 编辑器，OK，我就需要这个。

**修改默认编辑器**

```bash
$ git config --global core.editor "vim -u NONE"
```

**查看**

```bash
$ git config --list
...
core.editor=vim -u NONE
...
```

再试着运行 `git merge`，在纯净的 Vim 环境打开了合并信息，完美。
