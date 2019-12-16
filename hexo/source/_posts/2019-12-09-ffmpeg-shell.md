---
title: ffmpeg-shell
date: 2019-12-09 23:04:16
tags: [ffmpeg]
---

记录 FFmpeg 的一些命令

<!-- more -->
<!-- toc -->

**m3u8 格式文件转为 mp4**

```bash
$ ffmpeg -i "https://xxxx.com/20191005/WofkPuP1/1200kb/hls/index.m3u8" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 target.mp4
```

**分割视频**

```bash
# -ss 开始时间（可选）
# -t 结束时间（可选）
# source.mp4 视频源
# target.mp4 目标名称
$ ffmpeg -ss 00:12:00 -t 00:56:00 -i source.mp4 -vcodec copy -acodec copy target.mp4
```

**将字幕文件烧进视频文件中**

```bash
$ ffmpeg -i source.mkv -vf subtitles=source.srt output.mkv
```
