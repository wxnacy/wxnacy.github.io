---
title: Vim 插件 closetag 成对标签自动补全
date: 2017-09-25 11:36:18
tags: [vim]
---

[专辑：Vim 练级手册](/vim)


在 IDE 开发代码时，***xml, html*** 等成对标签都可以自动补全
在 Vim 中想要达到这样的效果需要借助插件 [closetag](https://github.com/docunext/closetag.vim)

<!-- more -->

<!-- toc -->
## 预览
![closetag](/images/closetag.gif)

## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/docunext/closetag.vim
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'docunext/closetag.vim'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
let g:closetag_html_style=1     " 支持 html 风格"
```

## 使用
被动技能
