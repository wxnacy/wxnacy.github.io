---
title: Vim 执行 Shell 命令（3）
date: 2019-05-17 17:40:56
tags: [vim]
---

上个月写了两篇 Vim 中使用 Shell 的文章，[Vim 执行 Shell 命令（1）](/2019/04/15/vim-run-shell/) 和 [Vim 执行 Shell 命令（2）](/2019/04/18/vim-in-shell/)，在 [typebrook](https://github.com/wxnacy/wxnacy.github.io/issues/1) 的提醒下发现还有 `:terminal` 可以实现，并且用了下发现还很好用。

<!-- more -->
<!-- toc -->

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell8.gif)

像预览中展示的这样，`:terminal` 可以切分出一个 terminal 来运行 shell 命令，这样的方式比前面的介绍的两种方式要更好，它类似 tmux 的多窗口操作，你也可以一边编写代码，一边执行命令。

打开命令如下

```vim
" 打开 terminal，水平分屏"
:terminal
:term
:ter

" 打开 terminal，垂直分屏"
:vertical terminal
:vert ter
```

关闭 terminal 可以直接输入 `exit` 然后回车，也可以直接使用 `<CTRL-D>`，我更喜欢使用后者。

打开 terminal 后，可以使用 `CTRL-W` 前缀键来进行窗口操作，正常使用 `<CTRL-W>n` 打开窗口后，怎么操作，terminal 就可以怎么操作，比如在垂直打开 terminal 后，使用 `<CTRL-W>h` 和 `<CTRL-W>l` 可以将光标在两个窗口中切换

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell9.gif)

打开 terminal 后，左下角显示的 `TERMINAL` 字样，此时我们无法直接对该窗口下的内容进行保存操作，因为它处于 `buftype` 下，我们可以使用另存为的方式将执行结果保存起来，比如 `<CTRL-W>:w newfile`，不过这时候有个问题，它会将 shell 环境下所有的显示内容都保存到文件中，包括你的输入命令和一些无关的显示文字。

这时候我们可以在打开 terminal 时，在命令后面跟上想要使用的 shell 命令，这时会将执行结果保存在缓存文件中并在 terminal 中打开。

```vim
:vert ter ls -l
```

该窗口仍然是缓存状态，所以不能直接保存，使用 `:w newfile` 另存为新文件即可，此时窗口左下角显示的是 `NORMAL`，我们不能再用 `<CTRL-D>` 关闭窗口了，只能使用 `:q` 来关闭。

![3](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell10.gif)

我介绍的三种方式都各有应用场景，综合来说 `:terminal` 是我在没有 tmux 情况的首选。

以上只是很简单的使用，也是比较常用的，它在 Vim 中是个大栏目，很多复杂的编辑器操作都可以通过它来完成，你可以阅读文档 `:h terminal` 来了解这些

不管你用了 Vim 多久，你总是会发现更多你不了解的功能，又学到了新东西，开心😊

- [terminal.txt](https://vimhelp.org/terminal.txt.html#terminal.txt)
