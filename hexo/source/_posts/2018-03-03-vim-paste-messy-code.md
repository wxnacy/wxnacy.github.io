---
title: Vim 解决复制黏贴格式错乱的问题
tags:
  - vim
date: 2018-03-03 16:19:33
---


Vim 让我头疼了很长时间的黏贴剪切版乱码的问题终于得到了解决，跟从 Vim 复制到剪切版是一样的道理，使用缓存区，妈蛋，为什么我没有早点想到。

<!-- more --><!-- toc -->
当复制系统内容后按键 `"+p` 即可将文本原格式黏贴到 Vim 中

方便的做法是使用 map 映射，修改 `~/.vimrc`
```vim
nnoremap <C-p> "+p
inoremap <C-p> <esc>"+pkddi
```
这样不管普通模式还是插入模式，使用 `<ctrl> + p` 既可以完成黏贴

- [Vim 复制粘贴探秘](http://www.worldhello.net/2010/12/08/2190.html)
