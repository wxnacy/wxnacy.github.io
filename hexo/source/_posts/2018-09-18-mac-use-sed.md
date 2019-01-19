---
title: Mac 使用 sed
date: 2018-09-18 11:41:51
tags: [mac]
---

在 Mac 中使用 sed 有很多问题。

<!-- more --><!-- toc -->
```bash
command i expects \ followed by text.
```

等错误都是 Mac 系统和 Linux 系统某些不同导致的

每个不适用的命令都可以有相应的解决办法，但是这样未免太过麻烦，有个可以一次解决的方法，借助 `brew` 即可完成。

安装 `gnu-sed`

```bash
$ brew install gnu-sed
```

安装后可以使用 `gsed` 命令进行 sed 的全部操作

如果不想使用 `gsed` 命令，在安装的时候可以使用参数 `--with-default-names` 来制定命令名

- [SED command error on MACOS X](https://stackoverflow.com/questions/14846304/sed-command-error-on-macos-x)
- [mac环境使用sed修改文件出错的解决方法](https://blog.csdn.net/fdipzone/article/details/51253955)
