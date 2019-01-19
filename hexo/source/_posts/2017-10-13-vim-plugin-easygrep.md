---
title: Vim 插件 EasyGrep 全局搜索文件
date: 2017-10-13 14:19:15
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

关于在 Vim 中使用 Grep 做全局搜索，我在文章[Vim 高级功能 vimgrep 全局搜索文件](/2017/10/13/vim-grep)中有介绍，
但是命令行和手动打开搜索结果都让人感觉很不方便，[EasyGrep](https://github.com/dkprice/vim-easygrep) 应运而生，
它基于 vimgrep 进行封装，让搜索变得更简单，EasyGrep 有快捷键和命令行两种使用方式

<!-- more -->

<!-- toc -->
## 预览
![/images/easygrep.gif](/images/easygrep.gif)
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/dkprice/vim-easygrep.git
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'dkprice/vim-easygrep'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 使用
### 快捷键
```bash
<Leader>vv  # 搜索光标所在单词，并匹配出所有结果，类似 gstar
<Leader>vV  # 搜索光标所在单词，全词匹配，类似 star
<Leader>va  # 类似 vv，但是会把结果添加到之前的搜索列表
<Leader>vA  # 类似 vV，但是会把结果添加到之前的搜索列表
<Leader>vr  # 全局搜索光标所在单词，并替换想要的单词
```
### 命令行
```bash
:Grep [arg]             # 类似 <Leader>vv，使用 ! 类似<Leader>vV
:GrepAdd [arg]          # 类似 <Leader>va，使用 ! 类似<Leader>vA
:Replace [target] [replacement] # 类似 <Leader>vr
:ReplaceUndo            # 撤销替换操作
```

更多使用[文档](https://github.com/dkprice/vim-easygrep#using-easygrep)
更多配置[文档](https://github.com/dkprice/vim-easygrep#using-easygrep-with-perl-style-regexp)
