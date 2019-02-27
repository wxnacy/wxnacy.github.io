---
title: Vimscript 判断文件是否存在
date: 2019-02-21 18:28:52
tags: [vim]
---

在 `~/.vimrc` 我希望可以通过判断当前环境是否含有某插件，再加载相应的参数配置，此时可以通过判断文件是否存在来完成。

<!-- more --><!-- toc -->

```vim
if filereadable('test.txt')    " 判断文件是否存在"
    echo 'file is exists'
endif
```

文件路径可以加上环境变量，用 `.` 链接

```vim
$HOME . '/.vim/bundle/jedi-vim/Makefile'
```

或者使用 `expand()` 函数

```vim
expand("$HOME/.vim/bundle/jedi-vim/Makefile")
```

完整代码

```vim
if filereadable(expand("$HOME/.vim/bundle/jedi-vim/Makefile"))    " 判断文件是否存在"
    echo 'jedi-vim is exists'
endif
```
