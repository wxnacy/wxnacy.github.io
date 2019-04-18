---
title: Vim 执行 Shell 命令（2）
date: 2019-04-18 22:08:20
tags: [vim]
---

前两天我写了在 Vim 中执行 Shell 命令，传送门 [Vim 执行 Shell 命令（1）](/2019/04/15/vim-run-shell/)

<!-- more -->
<!-- toc -->

今天我们来说如何在 Vim 和 Shell 间切换。

## `<ctrl-z>`

使用 `<ctrl-z>` 可以将当前 Vim 挂起，然后回到 Shell 模式，可以执行任何命令后，再使用 `fg` 或者 `fg %vim` 返回 Vim。

如果连续挂起多个，可以使用 `fg %1` 或者 `fg %vim filename` 回到 Vim。

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell5.gif)

这种方式来回切换多少有点不方便，直接使用 command 模式要更方便一点。

## :shell

```vim
:sh[ell]
```

输入该命令即可进入 Shell 环境，然后使用 `<ctrl-d>` 即可返回 Vim。

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell6.gif)

这个流程显得顺畅很多，另外我们可以使用映射来做到只用 `<ctrl-d>` 来回切换。

```vim
:noremap <c-d> :sh<cr>  " 修改映射"
```

这样虽然方便，但 `<ctrl-d>` 本来是向下翻半页，很挺常用的，是否要更换这个映射还有待斟酌。

因为 `:sh` 是主动进入 Shell 环境，所以它可以指定命令，比如你想使用 `fish` 则可以这样

```vim
:set shell=/usr/local/bin/fish
```

![3](https://raw.githubusercontent.com/wxnacy/image/master/blog/vim-shell7.gif)
