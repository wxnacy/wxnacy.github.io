---
title: FFmpeg 常用的命令
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

**mkv 格式转为 mp4**

```bash
$ ffmpeg -i input.mkv -c copy -strict -2 output.mp4
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

**将多个视频无损的合并为一个**

首先在视频目录下准备一个文件 `filename.txt` 内容为 

```bash
file 05-wodedipan.mkv
file 05-yuanyouhui.mkv
file 05-luanwuchunqiu.mkv
file 06-langmanshouji.mkv
file 06-lansefengbao.mkv
file 06-piaoyi.mkv
file 02-duibuqi.mkv
file 03-anhao.mkv
```

然后执行命令

```bash
$ ffmpeg -f concat -i filelist.txt -c copy output.mkv
```

***注意 filename.txt 中的文件名不能有中文***

`filename.txt` 可以使用命令行来直接生成，先把视频都放在同一文件夹下然后执行

```bash
$ ll | awk '{print "file" $9}' > filelist.txt
```

一般文件名我们都习惯取中文名，这里改成英文名也可以借助程序来批量修改。

这里需要用到 `Python` 来写一个脚本

首先下载依赖包

```bash
$ pip install pypinyin
```

然后在视频目录下运行该文件即可

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from pypinyin import lazy_pinyin
import os

def hans2py(hans):
    '''汉字转拼音'''
    hans = hans.lower()
    hans = hans.split()
    all_words = lazy_pinyin(hans)
    return all_words

dirs = os.listdir()

for d in dirs:
    pin = hans2py(d)
    os.rename(d, ''.join(pin))

```

