---
title: 不需要下载完整视频也可以获取时长
date: 2018-07-28 17:58:54
tags: [工具]
---

使用 ffmpeg 即可

<!-- more --><!-- toc -->

```bash
$ ffmpeg -i video_url 2>&1 | grep Duration | awk '{print $2}'
00:07:44.53,
```

这样获取到的是完整的时间格式，一般程序需要使用秒数，可以再改一下命令

```bash
$ ffprobe  -show_entries format=duration -v quiet -of csv="p=0" -i video_url
30.333
```

返回的是秒数，浮点型，可以使用程序在处理下

