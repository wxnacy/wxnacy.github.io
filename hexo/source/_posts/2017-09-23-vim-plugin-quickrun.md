---
title: Vim 插件 quickrun 快速运行
date: 2017-09-23 21:27:02
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

[quickrun](https://github.com/wklken/k-vim) 可以快速运行 ***.py/.sh*** 等常见程序
<!-- more -->

<!-- toc -->

## 预览
![quickrun](/images/quickrun.gif)

## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/wklken/k-vim
```
### Vundle
修改 `~/.vimrc`
```bash
Plugin 'wklken/k-vim'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
let g:quickrun_config = {
\   "_" : {
\       "outputter" : "message",
\   },
\}

let g:quickrun_no_default_key_mappings = 1
nmap <Leader>r <Plug>(quickrun)
map <F10> :QuickRun<CR>
```

## 使用
```bash
<leader>r 或 F10    # 可以运行程序，以 message 显示结果，任意键可返回
```
