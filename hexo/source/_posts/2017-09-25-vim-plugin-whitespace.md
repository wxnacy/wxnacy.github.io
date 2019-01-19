---
title: Vim 插件 vim-trailing-whitespace 去掉行尾空格
date: 2017-09-25 11:17:57
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

[vim-trailing-whitespace](https://github.com/bronson/vim-trailing-whitespace) 会将行尾空格标红，并可以一键去掉行尾的空格，python 开发和强迫症必备

<!-- more -->

<!-- toc -->
## 预览
![whitespace](/images/whitespace.gif)

## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/bronson/vim-trailing-whitespace
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'bronson/vim-trailing-whitespace'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
map <leader><space> :FixWhitespace<cr>
```

## 使用
```bash
<leader><space>     # 即可去掉全部行为空格
```
