---
title: Mac 系统实时显示键位操作软件：KeyCastr
date: 2018-12-11 11:51:58
tags: [mac]
---

最近想做一些 Vim 教程的视频，在屏幕上显示键位操作是很有必要的，网上找了下发现 KeyCastr 软件非常好用。

<!-- more --><!-- toc -->

## 预览
![key4](/images/KeyCastr4.gif)

## 安装
KeyCastr 是开源软件完全免费，源码可以在 [Github](https://github.com/keycastr/keycastr) 中找到，Mac 中安装非常方便

```bash
$ brew cask install keycastr
```

也可以从[下载](https://github.com/keycastr/keycastr/releases)页面下载最新版安装

## 配置
第一次使用时需要打开系统的辅助功能

![KeyCastr6](/images/KeyCastr6.png)

配置完成后再次打开，即可像预览中一样在屏幕左下角显示键位操作。

同时在顶部状态栏可以显示 KeyCastr 的图标，用于更多配置

![KeyCastr2](/images/KeyCastr2.png)

通过 Preferences -> General 配置可以修改图标展示在顶部或底部状态栏

![KeyCastr1](/images/KeyCastr1.png)

通过 Preferences -> Display 配置可以扩展显示区域，将 ⌘（Command）、⌥（Option）符号展示出来，很多人（包括我）经常会分不清楚他们对应的键位。

![KeyCastr5](/images/KeyCastr5.gif)

如下图，将显示模式改为 Svelte 即可

![KeyCastr3](/images/KeyCastr3.png)

默认情况下，该模式只显示四个特殊键位，勾选上 [Display all keystrokes] 即可显示全部键位
