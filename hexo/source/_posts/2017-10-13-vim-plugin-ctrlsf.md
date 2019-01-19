---
title: Vim 插件 CtrlSF 全局搜索文件
date: 2017-10-13 14:19:35
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

在 Vim 中搜索文件，使用 Ack 或 EasyGrep 已经足足的够了，
但是如果我们想把搜索做的更像 IDE ，比如把搜索命中行的上下几行也都显示出来那就更完美了，
这时候我们需要用到 [CtrlSF](https://github.com/dyng/ctrlsf.vim)
![/images/ctrlsf.gif](/images/ctrlsf.gif)
<!-- more -->

<!-- toc -->
## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/dyng/ctrlsf.vim.git
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'dyng/ctrlsf.vim'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
nmap <Leader><Leader>c :CtrlSF<space>
```

## 使用
使用快捷键 `<Leader><Leader>c` 唤出搜索命令后，输入关键词和文件名，
如：`:CtrlSF test *.py` 回车即可跳转到第一个匹配行，并列出搜索结果，并点击 `o` 跳转命中文件

## 参考文献
- [更多使用](https://github.com/dyng/ctrlsf.vim#key-maps)
