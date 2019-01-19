---
title: Vim 插件 tern_for_vim Javascript 自动补全
date: 2017-09-22 18:14:03
tags: [vim, javascript]
---

[专辑：Vim 练级手册](/vim)

在使用 Vim 开发的过程中，发现 仅仅使用 ***YouCompleteMe*** 并不能很好的支持 JavaScript 的自动补全
后来发现 ***Tern*** 可以跟 YouCompleteMe 很好的配合来完成自动补全
下面我来介绍 Tern 在 Vim 中的插件 [tern_for_vim](https://github.com/ternjs/tern_for_vim.git)
<!-- more -->

<!-- toc -->

## 预览
![tern](/images/tern.gif)
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/marijnh/tern_for_vim
```
### Vundle
在 `~/.vimrc` 中添加
```bash
Plugin 'marijnh/tern_for_vim'
```
在 Vim 中运行
```bash
:PluginInstall
```
## 配合 YouCompleteMe
安装完 Tern 后，需要 YouCompleteMe 在安装时传入支持 Tern 的参数
```bash
$ ./install.py --tern-complete
```
YouCompleteMe 的详细教程请参考我得文章 [Vim 插件 YouCompleteMe](/2017/09/22/vim-plugin-youcompleteme)

## 配置
Tern 是 NodeJs 项目，所以需要进行 `npm install` 操作
```bash
$ cd ~/.vim/bundle/tern_for_vim
$ npm install
```
完成后需要在项目的根目录建立 `.tern-project` 文件
或者在用户根目录 `~/` 下建立 `.tern-project` 文件
```json
{
    "ecmaVersion": 6,
    "libs": [
        "browser",
        "underscore",
        "jquery"
    ],
    "plugins": {
        "node": {}
    }
}
```
此时你已经可以打开 Vim 体验 JavaScript 的自动补全了

## 配置说明
```bash
ecmaVersion # 选择 ECMAScript 版本
libs        # browser 表示原生 js 补全，jquery 代表 jQuery 补全
loadEagerly # 指定加载解析的 js 文件
dontLoad    # 排除加载的文件
plugins     # ternjs 使用的插件，配置的扩展补全的库等
```
### libs
- browser
- chai
- ecma5，默认自动导入
- ecma6
- jquery
- underscore
