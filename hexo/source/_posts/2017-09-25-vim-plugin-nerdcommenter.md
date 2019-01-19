---
title: Vim 插件 nerdcommenter 快速注释
date: 2017-09-25 17:49:06
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

[nerdcommenter](https://github.com/scrooloose/nerdcommenter) 快速注释/解开注释
Vim 必备的插件

<!-- more -->

<!-- toc -->
![/images/nerdc.gif](/images/nerdc.gif)
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/scrooloose/nerdcommenter
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'scrooloose/nerdcommenter'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
let g:NERDSpaceDelims=1     " 注释后面自动加空格"
```

## 使用
```bash
<leader>cc   加注释
<leader>cu   解开注释

<leader>c<space>  加上/解开注释, 智能判断
<leader>cy   先复制, 再注解(p可以进行黏贴)
```
更多使用见[文档](https://github.com/scrooloose/nerdcommenter#usage)
