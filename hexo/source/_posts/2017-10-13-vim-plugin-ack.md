---
title: Vim 插件 Ack 全局搜索文件
date: 2017-10-13 14:19:26
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

简单项目使用 vimgrep 或 EasyGrep 已经足够完成搜索任务，但是在一些大型项目中 grep 的搜索速度就跟不上了，这时候可以使用 [Ack](https://github.com/mileszs/ack.vim) 替代它完成搜索任务
<!-- more -->

<!-- toc -->
## 预览
![ack](/images/ack.gif)
## 安装
首先需要在机器上安装 Ack 工具
Mac
```bash
$ brew install ack
```
完成后安装 Vim 插件
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/mileszs/ack.vim.git
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'mileszs/ack.vim'
```
在 Vim 中运行
```bash
:PluginInstall
```
## 使用
命令
```bash
:Ack [options] {pattern} [{directories}]
```
还可以像 `:grep`, `:grepadd`, `:lgrep`, `:lgrepadd` 一样使用 `:Ack`, `:AckAdd`, `:LAck`, `:LAckAdd`

## 配置
可以在有 `ag` 时使用 ag 进行搜索
```bash
if executable('ag')
    let g:ackprg = 'ag --nogroup --nocolor --column'
endif
```
快捷键
```bash
nmap <Leader><Leader>a :Ack<space>-i<space>     # -i 忽略大小写
```

## 参考文献
- [更多使用](https://github.com/mileszs/ack.vim#keyboard-shortcuts)
- [何不 Ack？Grep, Ack, Ag的搜索效率对比](https://linux.cn/article-5077-1.html)
