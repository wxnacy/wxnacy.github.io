---
title: Vim 插件 vim-surround 单词加环绕符号
date: 2017-09-25 10:40:43
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

> [vim-surround](https://github.com/tpope/vim-surround) 可以给单词或句子加上各种标签符号

<!-- more -->

<!-- toc -->
![/images/surround.gif](/images/surround.gif)
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/tpope/vim-surround
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'tpope/vim-surround'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 使用
```bash
cs"'            # 替换 ==> "Hello world!" -> 'Hello world!'
cst"            # 替换-标签(t=tag)  ==> <a>abc</a>a>  -> "abc"
cst<html>       # 替换标签 ==> <a>abc</a>a>  -> <html>abc</html>html>
ds"             # 删除  ==> "Hello world!" -> Hello world!
ysiw"           # 添加(ys=you surround) ==> Hello -> "Hello"
csw"            # 添加  ==> Hello -> "Hello"
veeS"           # 添加-两个词   ==> hello world -> "hello world"
ys$"            # 添加-当前到行尾:
yss"            # 添加-整行 ==> Hello world -> "Hello world"
ySS"
Hello world ->
"
    hello world
"

# 左符号/右符号 => 带不带空格
cs([
(hello) -> [ hello  ]

cs(]
(hello) -> [hello])
])
```
