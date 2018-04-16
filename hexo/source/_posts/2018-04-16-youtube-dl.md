---
title: 使用 youtube-dl 下载视频
tags:
  - 工具
date: 2018-04-16 14:18:56
---


> 可以从视频网站下载视频的命令行程序

<!-- more --><!-- toc -->

## 下载

**curl**

```bash
$ sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
$ sudo chmod a+rx /usr/local/bin/youtube-dl
```

**wget**

```bash
$ sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
$ sudo chmod a+rx /usr/local/bin/youtube-dl
```

**pip**

```bash
$ sudo pip install --upgrade youtube_dl
```

**Homebrew**

```bash
$ brew install youtube-dl
```

## 使用

```bash
$ youtube-dl [OPTIONS] URL [URL...]
```

**无参数**，模式下载 `720p` 的视频

```bash
$ youtube-dl https://www.youtube.com/watch\?v\=IYMqASfrvKY
```

**查看可以下载的格式**

```bash
$ youtube-dl -F https://www.youtube.com/watch\?v\=IYMqASfrvKY
```

**下载指定格式**

```bash
$ youtube-dl -f 137 https://www.youtube.com/watch\?v\=IYMqASfrvKY
```

**程序升级**

```bash
$ youtube-dl -U
```

**查看支持的网站**

```bash
$ youtube-dl --list-extractors
```

更多用法见[文档](https://github.com/rg3/youtube-dl/#options)

- [youtube-dl 使用小记](http://www.cnblogs.com/faunjoe88/p/7810427.html)
