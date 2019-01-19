---
title: Vim 插件 vim-airline 状态栏增强显示
date: 2017-09-25 14:41:18
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

[vim-airline](https://github.com/bling/vim-airline) 状态栏增强显示
先来看效果
![airline](/images/airline.png)

<!-- more -->

<!-- toc -->
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/bling/vim-airline
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'bling/vim-airline'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
if !exists('g:airline_symbols')
let g:airline_symbols = {}
endif
let g:airline_left_sep = '▶'
let g:airline_left_alt_sep = '❯'
let g:airline_right_sep = '◀'
let g:airline_right_alt_sep = '❮'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'

" 是否打开tabline
let g:airline#extensions#tabline#enabled = 1 # 打开后，tabline和tmuxline都可以得到增强
```
airline 还可以支持很多插件如 ***virtualenv, tmux*** ，更多见[ 文档 ](https://github.com/bling/vim-airline#features)
