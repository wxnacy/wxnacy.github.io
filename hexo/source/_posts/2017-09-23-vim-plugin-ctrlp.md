---
title: Vim 插件 ctrlp.vim 模糊搜索文件
date: 2017-09-23 20:09:57
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

> Vim 中的 find

<!-- more -->

<!-- toc -->
我认为是 Vim 中必不可少的插件，作用是可以模糊搜索文件 ***/buf/mru/tag*** 等等
我用的是改进版的 [ctrlpvim/ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim) 原版是 [kien/ctrlp.vim](https://github.com/kien/ctrlp.vim)

## 预览
![ctrlp](/images/ctrlp.gif)

## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/kien/ctrlp.vim
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'kien/ctrlp.vim'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
let g:ctrlp_map = '<leader>p'
let g:ctrlp_cmd = 'CtrlP'
map <leader>f :CtrlPMRU<CR>
let g:ctrlp_custom_ignore = {
    \ 'dir':  '\v[\/]\.(git|hg|svn|rvm)$',
    \ 'file': '\v\.(exe|so|dll|zip|tar|tar.gz|pyc)$',
    \ }
let g:ctrlp_working_path_mode=0
let g:ctrlp_match_window_bottom=1
let g:ctrlp_max_height=15
let g:ctrlp_match_window_reversed=0
let g:ctrlp_mruf_max=500
let g:ctrlp_follow_symlinks=1
```

## 使用
```bash
<leader>f   # 模糊搜索最近打开的文件(MRU)
<leader>p   # 模糊搜索当前目录及其子目录下的所有文件
```
搜索框出来后，输入关键词，然后可以做如下操作
```bash
ctrl + j/k  # 进行上下选择
ctrl + x    # 在当前窗口水平分屏打开文件
ctrl + v    # 同上, 垂直分屏
ctrl + t    # 在tab中打开
```
在搜索框状态下，还可以进行额外操作
```bash
F5          # 刷新可搜索文件
<c-d>       # 只能搜索全路径文件
<c-r>       # 可以使用正则搜索文件
```
更多操作见 [文档](https://github.com/ctrlpvim/ctrlp.vim#basic-usage)

## ctrlp 的插件 ctrlp-funky
[ctrlp-funky](https://github.com/tacahiroy/ctrlp-funky) 可以模糊搜索文件内容的方法名

## 预览
![ctrlpfu](/images/ctrlpfu.gif)

### 安装
Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/tacahiroy/ctrlp-funky
```
Vundle
```bash
Plugin 'tacahiroy/ctrlp-funky'
```

### 配置
```bash
nnoremap <Leader>fu :CtrlPFunky<Cr>
" narrow the list down with a word under cursor
nnoremap <Leader>fU :execute 'CtrlPFunky ' . expand('<cword>')<Cr>
let g:ctrlp_funky_syntax_highlight = 1

let g:ctrlp_extensions = ['funky']
```

### 使用
```bash
<leader>fu      # 进入当前文件的函数列表搜索
<leader>fU      # 搜索当前光标下单词对应的函数
```
