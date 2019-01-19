---
title: Vim 插件 Emmet web 开发神器
date: 2018-03-25 17:17:10
tags:
---


最近开发些 web 页面，忍着敲标签的痛苦，想起来以前用过但不熟练的插件 [Emmet](https://emmet.io/)，用完以后在写起代码感觉欲罢不能。

<!-- more --><!-- toc -->
![/images/emmet.gif](/images/emmet.gif)

相信你在看过这个预览后，一定想开始尝试着用这个插件了，我们开始吧

## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/mattn/emmet-vim.git
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'mattn/emmet-vim'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
官方默认的快捷键前缀是 `<C-Y>`，这在按第三个键位的时候简直逆天，官方自己也说用户可以改成 `<C-Z>` 比较方便
```bash
let g:user_emmet_leader_key='<C-Z>'     " 设置快捷键
```

## 使用
insert 模式下输入 `html:5` 后键入快捷键 `<c-z>,` 完成代码键入
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title></title>
</head>
<body>

</body>
</html>
```
normal 模式下选中多行 `item`，键入快捷键 `<c-z>,` 完成代码键入
```html
  <ul>
    <li>
      <a href="">item</a>
    </li>
    <li>
      <a href="">item</a>
    </li>
    <li>
      <a href="">item</a>
    </li>
  </ul>
```
insert 模式后输入 `ul>li*3>a`，键入快捷键 `<c-z>,` 完成代码键入
```html
  <ul>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
  </ul>
```
更多使用见[文档](https://raw.githubusercontent.com/mattn/emmet-vim/master/TUTORIAL)
