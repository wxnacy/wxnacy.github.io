---
title: mac清除DNS缓存
date: 2017-08-10
tags: [mac]
---

原文：[https://support.apple.com/zh-cn/HT202516](https://support.apple.com/zh-cn/HT202516)
## 关于 DNS 缓存
OS X 会将已解析的 DNS 查询的本地缓存保留一段时间，保留时间由 DNS 服务器定义。有时可能需要立即还原缓存设置并重新查询 DNS 服务器。例如，如果您是网络或服务器管理员且您的 DNS 服务器上的条目最近有更改，您可能需要执行此操作。
如果您的 Mac 使用的不是您服务器上的最新 DNS 条目，您可重新启动 Mac 以更新其缓存的信息。如果您需要更新使用 OS X 的服务器上的 DNS 条目但又不能重新启动服务器，请使用以下适用于您所使用的 OS X 版本的命令。
## OS X Yosemite及更新机型
在 OS X v10.10.4 或更高版本中，请使用以下“终端”命令来还原 DNS 缓存设置：
```bash
sudo killall -HUP mDNSResponder
```
在 OS X v10.10 至 v10.10.3 中，请使用以下“终端”命令来还原 DNS 缓存设置：
```bash
sudo discoveryutil mdnsflushcache
```
## OS X Mavericks、Mountain Lion 和 Lion
在 OS X v10.9.5 及更低版本中，请使用以下“终端”命令来还原 DNS 缓存设置：
```bash
sudo killall -HUP mDNSResponder
```
## Mac OS X Snow Leopard
在 OS X v10.6 至 v10.6.8 中，请使用以下“终端”命令来还原 DNS 缓存设置：
```bash
sudo dscacheutil -flushcache
```


