---
title: Vim 插件 gundo 代码回滚
date: 2017-09-25 11:04:11
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

成熟健壮的 IDE 都有本地代码回滚的功能，
[gundo](https://github.com/sjl/gundo.vim) 也可以帮助 Vim 实现查看历史记录和回滚的功能

<!-- more -->

<!-- toc -->
## 预览
![gundo](/images/gundo.gif)
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/sjl/gundo.vim
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'sjl/gundo.vim'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
nnoremap <leader>h :GundoToggle<CR>
```

## 使用
```bash
<leader>h   # 打开或关闭 gundo 界面
j/k         # 上下选择
p           # 查看diff
回车        # 回滚文件到这个时刻的版本
```
找回代码只限于本地编辑，如果 `:q` 退出过，就找不回来了
