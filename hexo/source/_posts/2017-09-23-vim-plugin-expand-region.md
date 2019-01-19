---
title: Vim 插件 expand-region 区域选中
date: 2017-09-23 21:41:31
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

[expand-region](https://github.com/terryma/vim-expand-region) 可以快速选中临近区域

<!-- more -->

<!-- toc -->

## 预览
![er](/images/expand-region.gif)

## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone https://github.com/terryma/vim-expand-region
```

### Vundle
修改 `~/.vimrc`
```bash
Plugin 'terryma/vim-expand-region'
```
在 Vim 中运行
```bash
:PluginInstall
```

## 配置
```bash
vmap v <Plug>(expand_region_expand)
vmap V <Plug>(expand_region_shrink)
```
我修改了官方快捷键，使用 `v, V` 更符合进入选中模式的习惯，更多配置见 [文档](https://github.com/terryma/vim-expand-region#setting)

## 使用
```bash
v   # 增加选中范围
V   # 减少选中范围
```
