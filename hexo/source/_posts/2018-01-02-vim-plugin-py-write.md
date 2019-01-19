---
title: Vim 如何编写插件：使用 Python 编写插件
date: 2018-01-02 15:59:21
tags: [vim]
---

前两天我讨论了怎么使用 Vim 编写最简单的插件 Hello World，今天聊聊怎么使用 Python 辅助插件开发，这在辅助开发插件时很有用。

<!-- more --><!-- toc -->
VimScript 语言非常小众，在处理一些数据时也不如我们常见的语言，如：Python／Ruby 等方便
```bash
$ vim --version
```
```bash
VIM - Vi IMproved 8.0 (2016 Sep 12, compiled Feb 12 2017 23:20:31)
MacOS X (unix) version
Included patches: 1-329
Compiled by Homebrew
Huge version without GUI.  Features included (+) or not (-):
+acl             +file_in_path    +mouse_sgr       +tag_old_static
+arabic          +find_in_path    -mouse_sysmouse  -tag_any_white
+autocmd         +float           +mouse_urxvt     -tcl
-balloon_eval    +folding         +mouse_xterm     +termguicolors
-browse          -footer          +multi_byte      +terminfo
++builtin_terms  +fork()          +multi_lang      +termresponse
+byte_offset     -gettext         -mzscheme        +textobjects
+channel         -hangul_input    +netbeans_intg   +timers
+cindent         +iconv           +num64           +title
-clientserver    +insert_expand   +packages        -toolbar
+clipboard       +job             +path_extra      +user_commands
+cmdline_compl   +jumplist        +perl            +vertsplit
+cmdline_hist    +keymap          +persistent_undo +virtualedit
+cmdline_info    +lambda          +postscript      +visual
+comments        +langmap         +printer         +visualextra
+conceal         +libcall         +profile         +viminfo
+cryptv          +linebreak       +python          +vreplace
+cscope          +lispindent      -python3         +wildignore
+cursorbind      +listcmds        +quickfix        +wildmenu
+cursorshape     +localmap        +reltime         +windows
+dialog_con      -lua             +rightleft       +writebackup
+diff            +menu            +ruby            -X11
+digraphs        +mksession       +scrollbind      -xfontset
-dnd             +modify_fname    +signs           -xim
-ebcdic          +mouse           +smartindent     -xpm
+emacs_tags      -mouseshape      +startuptime     -xsmp
+eval            +mouse_dec       +statusline      -xterm_clipboard
+ex_extra        -mouse_gpm       -sun_workshop    -xterm_save
+extra_search    -mouse_jsbterm   +syntax
+farsi           +mouse_netterm   +tag_binary
```
执行查看版本命令可以看到它支持的语言列表，Python 就在其中。

之所以选择 Python 语言，除了现在我主用 Python 开发外，主要是因为它的入门比大多书语言都比较简单，并且功能强大。GitHub 上很多开源插件都是 Python 辅助开发的，另外现在大火的人工智能，Python 也是首选的开发语言。

## Hello World
如果你还没有看前篇 [Vim 如何编写插件：Hello World](/2017/12/30/vim-plugin-write-helloworld/) ，建议先看下，不然可能不知道再说什么。
```vim
python << EOF
def helloworld():
    print("Hello World")
EOF

command! -nargs=0 Hw exec('py helloworld()')
```
我们同样是从 Hello World 来说

首先我们可以看到 Python 的函数是包在 `python << EOF ... EOF` 中的，这是一个标准写法，告诉 Vim 这是一个 Python 方法，`EOF` 不是固定的，换成任意字符都可，前后统一即可

在执行时，使用 `exec` 函数执行 Python 命令 `py helloworld()`

它跟 VimScript 写插件就在这两点不同，剩下的就可以像 Python 一样愉快的开发了。

如果你的 Vim 版本是小于 8 ，可能支持的语言列表这样的 `... -python, +python3` ，这是告诉你支持 Python3 ，不支持 Python，不用奇怪，在 Python 中 3 和以前的版本的变化很大，很多时候可以当两种语言处理。这时我们需要做如下改变。
```vim
python3 << EOF
def helloworld():
    print("Hello World")
EOF

command! -nargs=0 Hw exec('py3 helloworld()')
```
## 传参
看过上一章的传参，这里就很好理解了
```vim
:Hw name age
```
```vim
python << EOF
def helloworld(*args):
    print(args)     " ==> (name, age, )
EOF

command! -nargs=* Hw exec('py helloworld(<q-args>)')
```
通过对比发现，不管各方面，使用一个趁手的第三方语言来开发都要更方便一点。
## vim 模块
在 Vim 中 Python 有个特殊模块 vim
```vim
python << EOF
import vim
def helloworld():
    print(vim.current.buffer)   " 当前缓冲区
    vim.command(vim-cmd)        " 执行 vim 命令
EOF
command! -nargs=0 Hw exec('py helloworld()')
```
这个模块可以很方便的在 Python 中处理 Vim 的信息和指令，更多用法见文档 `:h python-vim`
