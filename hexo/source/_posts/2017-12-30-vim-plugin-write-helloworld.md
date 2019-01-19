---
title: Vim 如何编写插件：Hello World
date: 2017-12-30 16:28:41
tags: [vim]
---

从 8 月开始使用 Vim 已经 4 个多月了，从开始的笨拙查找按键，到后来健“指”如飞，再到开始编写插件，现在我已经离不开 Vim 了，我只需要几个按键就可以完成别人鼠标键盘配合半天才能完成的操作。

<!-- more --><!-- toc -->
两个月前，因为工作的原因我编写了插件 [vim-mysql](https://github.com/wxnacy/vim-mysql) ，我可以执行文本中某一行或者选中的一段完整语句。为什么要造“轮子”呢？即使现在的数据库软件再强大，它也是为大多人设计的，为了方便我就是需要一些独特的功能，所以可以编写一个自己用的工具很重要。
今天开始我们来探讨下，如何在 Vim 中编写插件
## Hello World
又是 Hello World ，没错，学什么开始都是 Hello World 。首先明确目标，今天要达到的目标是，用 Vim 打开任意文件后，通过简短指令输出 `Hello World`
首先在任意位置建立文件，如 `~/helloworld.vim`
```vim
function! HelloWorld()
    echo 'Hello World'
endfunction
```
在 `~/.vimrc` 中做链接，指定 Vim 再启动时运行该文件
```vim
source ~/helloworld.vim
```
执行 `:source ~/.vimrc` 使配置生效，或者干脆退出文件，再重新进入即可，随后执行 `call HelloWorld()` 并回车，既可以看到屏幕下方输出 `Hello World`，就是这么简单。
## 优化
任务是完成了，但是还可以在处理的更好一点，比如我改变一下插件的位置
```bash
~/.vim/plugin/helloworld.vim
```
同时我去掉这句 `source ~/helloworld.vim` ，你在此重复上边的执行操作，同样可以生效，因为他可以自动查找该文件夹的脚本自动导入。
再比如，我可以在插件里加上如下配置
```vim
function! HelloWorld()
    echo 'Hello World'
endfunction
command! -nargs=0 HW call HelloWorld()
nnoremap <leader>hw :call HelloWorld()
```
让代码生效后，我只需要执行 `:HW` 或者 `<leader>hw` 即可完成命令的调用。`-nargs=0` 表示命令行后边不跟参数，`<leader>` 键我在 [Vim 高级功能 Mapping 映射](/2017/12/01/vim-mappings/#leader) 文章中有详细讲解。
## 传参
在 VimScript 中传参是很别扭的
```vim
:HW name age
```
```vim
function! HelloWorld(cmd, args)
    echo a:cmd      " ==> grep
    echo a:args     " ==> name age
    echo a:args[0]  " ==> name
endfunction
command! -nargs=* HW call HelloWorld('grep', <q-args>)
```
```vim
function! HelloWorld(...)
    echo a:000  " ==> name age
    echo a:0    " ==> name
    echo a:1    " ==> age
endfunction
command! -nargs=* HW call HelloWorld(<q-args>)
```
这是固定参数加可变参数，已经完成可变参数的两种用法，`a:` 是参数前边必须加的。

`-nargs` 后可以跟的参数为 `0, 1, +, *, ?` 这些符号都可以当作正则表达式来理解，具体含义你可以查看文档 `:h command-nargs`

## 注意
有这么几点需要注意
- `HelloWorld` 函数名首字母必须大写
- `HW` command 执行的命令，首字母必须大写
- `helloworld.vim` 插件名比如用 `.vim` 后缀
还有就是在命令中频繁出现的 `!`，因为每次启动 Vim 都会执行插件里的代码，它的作用就是避免重复执行。现在不加它没有什么影响，但是如果你的插件越来越多，你会慢慢感觉到卡，那时候你都不知道哪里出的问题，所以我建议从一开始就养成好习惯。
