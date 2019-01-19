---
title: Vim 插件 vim-repeat 重复插件操作
date: 2017-09-25 10:40:59
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

> [vim-repeat](https://github.com/tpope/vim-repeat) 重复一个插件的操作

<!-- more -->

<!-- toc -->
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/tpope/vim-repeat
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'tpope/vim-repeat'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 使用
使用 `.` 即可重复操作，支持 [vim-surround](/2017/09/25/vim-plugin-surround/)
更多支持列表见 [文档](https://github.com/tpope/vim-repeat#repeatvim)
