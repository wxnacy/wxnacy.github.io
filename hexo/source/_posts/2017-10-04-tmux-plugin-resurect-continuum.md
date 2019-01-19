---
title: Tmux 插件 resurect & continuum 会话定时保存
date: 2017-10-04 09:44:13
tags: [tmux]
---

Tmux 好用，但是在电脑重启后，之前开启过的回话都不会保存，
而 [tmux-resurect](https://github.com/tmux-plugins/tmux-resurrect) 和 [tmux-continuum](https://github.com/tmux-plugins/tmux-continuum) 可以很好的自动保存 Tmux 使用状态
<!-- more -->

<!-- toc -->

## Tmux Resurect
### 安装
Tmux Plugin Manager
修改 .tmux.conf
```bash
set -g @plugin 'tmux-plugins/tmux-resurrect'
```
随后使用 `prefix + I` 进行安装

### 使用
```bash
prefix <c-s>    # 保存，Tmux 状态栏会显示“Saving。。。” 字样，完毕后即为保存
prefix <c-r>    # 还原 Tmux 状态
```
这样只要养成手动保存的习惯，就可以实时保存 Tmux 的状态，
但是我们仍然希望可以自动保存，这时候我们需要用到 Tmux Continuum

## Tmux Continuum
### 安装
Tmux Plugin Manager
修改 .tmux.conf
```bash
set -g @plugin 'tmux-plugins/tmux-continuum'
```
随后使用 `prefix + I` 进行安装

Tmux Continuum 默认十五分钟备份一次，可以自己修改
```bash
set -g @continuum-save-interval '60' # 修改为一小时
```
然后使用 `tmux source-file ~/.tmux.conf` 命令重载 Tmux 配置

两个插件都需要 Tmux >= 1.9 才行
