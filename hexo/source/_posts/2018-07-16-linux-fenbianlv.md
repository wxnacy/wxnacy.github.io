---
title: Linux 桌面版 修改分辨率
date: 2018-07-16 15:18:24
tags: [linux]
---

在使用虚拟机来运行 Linux 桌面版，上来这个分辨率实在是让人无法忍受。

<!-- more --><!-- toc -->
所以第一件事就是要修改分辨率

```bash
$ xrandr

Screen 0: minimum 1 x 1, current 800 x 600, maximum 8192 x 8192
Virtual1 connected primary 800x600+0+0 (normal left inverted right x axis y axis) 0mm x 0mm
   800x600       60.00*+  60.32
   2560x1600     59.99
   1920x1440     60.00
   1856x1392     60.00
   1792x1344     60.00
   1920x1200     59.88
   1600x1200     60.00
   1680x1050     59.95
   1400x1050     59.98
   1280x1024     60.02
   1440x900      59.89
   1280x960      60.00
   1360x768      60.02
   1280x800      59.81
   1152x864      75.00
   1280x768      59.87
   1024x768      60.00
   640x480       59.94
Virtual2 disconnected (normal left inverted right x axis y axis)
Virtual3 disconnected (normal left inverted right x axis y axis)
Virtual4 disconnected (normal left inverted right x axis y axis)
Virtual5 disconnected (normal left inverted right x axis y axis)
Virtual6 disconnected (normal left inverted right x axis y axis)
Virtual7 disconnected (normal left inverted right x axis y axis)
Virtual8 disconnected (normal left inverted right x axis y axis)
```

`xrandr` 命令可以操作分辨率，列表中带有 `*` 号的就是当前正在使用的分辨率

```bash
$ xrandr -s 5
```

它的索引是从 0 开始的，输入目标数字即可切换分辨率
