" 快捷输入 {{{
iabbrev <buffer> h1 #
iabbrev <buffer> h2 ##
iabbrev <buffer> h3 ###
iabbrev <buffer> h4 ####

iabbrev <buffer> `b ```bash<cr>```<esc>O
iabbrev <buffer> `p ```python<cr>```<esc>O#!/usr/bin/env python<cr>
            \# -*- coding:utf-8 -*-<cr>
            \# Author: wxnacy(wxnacy@gmail.com)<cr>
iabbrev <buffer> `j ```java<cr>```<esc>O
iabbrev <buffer> `v ```vim<cr>```<esc>O
iabbrev <buffer> `m ```mysql<cr>```<esc>O

iabbrev <buffer> mt <!-- more --><!-- toc --><cr>

iabbrev <buffer> pi <!-- more --><cr><!-- toc --><cr>## 安装<cr> ### Pathogen
            \<cr>```bash<cr>$ cd ~/.vim/bundle<cr>$ git clone <cr>```<cr>
            \### Vundle<cr>修改 `~/.vimrc`<cr>```bash<cr>Plugin ''<cr> ```<cr>
            \在 Vim 中运行<cr>```bash<cr>:PluginInstall<cr>```<cr>## 配置<cr>
            \```bash<cr>```<cr>## 使用<cr>```bash<cr>```

" }}}
