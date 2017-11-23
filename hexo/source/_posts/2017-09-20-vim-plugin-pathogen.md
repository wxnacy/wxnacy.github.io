---
title: Vim 插件 pathogen 插件管理
date: 2017-09-20 15:00:12
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

> pathogen 更好的插件管理方案

<!-- more -->
改用 vim 做主开发工具有一段时间了，之前一直在用 [Vundle](https://github.com/VundleVim/Vundle.vim)
管理插件回想起用 Vundle 装第一个插件，当时的痛苦现在还历历在目，对于一个新手来
说去哪里写 `:PluginInstall` 都折腾了好久 pathogen 可以将插件都集中管理到
***~/.vim/bundle*** 中，并且各个插件都拥有自己的目录（这点 Vundle 也可以做到），
他的优点在于只依赖与 git 来管理插件，无需在 vim 做过多的配置

## 安装
```bash
$ mkdir .vim && cd .vim
$ mkdir bundle && mkdir autoload && cd bundle
$ git clone https://github.com/tpope/vim-pathogen.git
$ cp vim-pathogen/autoload/pathogen.vim ~/.vim/autoload/
```

## 配置
在 ***~/.vimrc*** 文件里, `filetype plugin indent on` 之前的任何地方，加入这句
：`call pathogen#infect()`

这样 pathogen 就已经安装完成了，接下来我们下载一个插件看下效果

## 第一个插件
```bash
$ cd ~/.vim/bundle
$ git clone http://github.com/scrooloose/nerdtree.git
```
执行完两条命令后，bundle 文件夹中就会出现 nerdtree 文件，
这样就已经安装完成，pathogen 会自动加载 bundle 中的插件

## 更新插件
如果想要更新某个插件，只需要进入到相应插件目录 `~/.vim/bundle/nerdtree` 中执行
下拉命令
```bash
$ git pull
```
如果插件特别多，不想一个一个下拉代码，也可以使用 Git 的 ***submodule*** 模块
托管到 GitHub 中
在我的文章 [Git 工具 submodule](/2017/09/19/git-submodule) 中有介绍

## 删除插件
删除插件也很简单，需要进入 ***~/.vim/bundle*** 执行删除目录命令即可
```bash
$ rm -rf nerdtree
```
