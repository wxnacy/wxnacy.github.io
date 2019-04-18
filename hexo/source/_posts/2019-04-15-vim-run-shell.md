---
title: Vim 执行 Shell 命令（1）
date: 2019-04-15 21:50:52
tags: [vim]
---

Vim 编写程序时，无须退出 Vim 或者新建 Terminal 窗口即可执行 Shell 命令。

<!-- more -->

在 Mac 环境开发时，可以使用 Tmux 搭配 Vim，一个窗口编写，一个窗口执行。然而线上环境往往不能安装过于复杂的开发环境，那每次都反复的进入退出很是让人烦躁，其实 Vim 中可以直接运行 Shell 命令。

<!-- toc -->

## 执行

**语法**

```vim
:!command
```

`command` 可以是任何一个 Shell 命令，回车执行后，会在 Shell 中显示结果，再次回车返回 Vim。先来看个动图

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell1.gif)

## 读取

该模式下还可以直接把执行结果，读取到 Vim 中，这是很神奇的功能。

**语法**

```vim
:r !command
```

执行该命令后，Shell 命令结果会自动复制到当前行的下面

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell2.gif)


前面输入数字，可以复制到第 N 行的下面，比如第二行

```vim
:2r !command
```

## 写入

能读取，就能写入，使用 `w` 可以将制定行数的文本通过管道传给想要执行的命令

**语法**

```vim
:n1, n2w !command
```

比如我们想要将第 7 到 10 行的内容传给 `wc` 命令，获取行数，单词数和字符数。

```vim
:7, 10w !wc
```

![3](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell3.gif)

## 替换

最后要说的是替换，它好像将上边两种命令结合一般，这次直接输入行数范围即可

```vim
:n1, n2 !wc
```

还是上面的例子，我们重新执行一次

![4](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell4.gif)

最后提一句 `:!!` 可以执行上一次执行的命令，没错，就像 Shell 中一样。

直接在 Vim 中执行 Shell 命令，只是一种方式，我们还可以直接切换到 Shell 模式在执行复杂的操作。

不过今天先到这里，想要学好 Vim，一次输入太多知识不是个好习惯，还需要大量的练习来巩固它，下一章我们再来探讨怎样切换 Shell 环境。

传送门 [Vim 执行 Shell 命令（2）](/2019/04/18/vim-in-shell/)
