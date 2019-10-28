---
title: Mac 使用 vmware 装机报错 /dev/vmmon：Broken pipe
tags:
  - mac
  - vmware
date: 2019-10-28 08:14:44
---


好久不用虚拟机了，最近想装个 win10 调试程序，结果各种问题，记录下以备后用。

<!-- more -->
<!-- toc -->

在加载镜像后，启动前一直莫名报这个错。

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/vm-error1.png)

问题出在 Mac 禁止了 VMware 的一些功能，可以进入 `系统偏好设置 -> 安全性与隐私 -> 通用`，然后点击下方的允许即可。

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/vm-error2.png)
