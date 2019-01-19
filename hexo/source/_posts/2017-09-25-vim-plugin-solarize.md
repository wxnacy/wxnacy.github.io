---
title: Vim 插件 vim-colors-solarized 主题
date: 2017-09-25 15:54:43
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

[vim-colors-solarized](https://github.com/altercation/vim-colors-solarized) 不用多说现在最流行的 Vim 主题

<!-- more -->

<!-- toc -->
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/altercation/vim-colors-solarized
```
因为 Vim 配色是读取的 `~/.vim/colors` 目录下，所以还需要一步复制操作
```bash
$ cp ~/.vim/bundle/vim-colors-solarized/colors/solarized.vim ~/.vim/colors/
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'altercation/vim-colors-solarized'
```
在 Vim 中运行
```bash
:PluginInstall
```
复制操作跟 Pathogen 相同

## 配置
```bash
set background=dark
set t_Co=256
colorscheme solarized
```
重新打开 Vim 即可看到效果
