---
title: 使用 youtube-dl 下载油管视频
tags:
  - python
  - 工具
date: 2019-09-15 14:56:00
---


油管上有全球最大的视频资源库，由于一些限制我们不能随时随地看到，如果有机会看的时候，也能批量下载一些视频就非常 nice 了， [youtube-dl](https://github.com/ytdl-org/youtube-dl) 可以完美的实现这个需求

<!-- more -->
<!-- toc -->

## 下载

### pip

```bash
$ sudo -H pip install --upgrade youtube-dl
```

### Linux

```bash
$ sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
$ sudo chmod a+rx /usr/local/bin/youtube-dl
```

### Mac

```bash
$ brew install youtube-dl
```

### Windows

下载 [youtube-dl.exe](https://yt-dl.org/latest/youtube-dl.exe) 文件直接运行即可。

这里有点需要注意，如果你是 Windows10 系统，很可能会报一个找不到 `MSVCR100.dll` 的错误，此时需要先安装 [Microsoft Visual C++ 2010 Redistributable Package (x86)](https://www.microsoft.com/en-US/download/details.aspx?id=5555)，然后再次执行 `youtube-dl.exe` 即可

## 下载视频

```bash
$ youtube-dl https://www.youtube.com/watch?v=OKIfTOEo7P0
```

下载视频就是这么简单，默认下载的是 720p 的视频，只要你有的话，我们也可以先看下视频都包含什么格式

```bash
$ youtube-dl -F https://www.youtube.com/watch?v=OKIfTOEo7P0
```

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/ytdl1.png)

也可以指定下载 1080p 的视频，使用第一列的数字可以精准下载

```bash
$ youtube-dl -f 137 https://www.youtube.com/watch?v=OKIfTOEo7P0
```

有时候默认情况下会下载 webm 格式的视频，我们可以设置只下载 mp4 格式的视频

```bash
$ youtube-dl -f mp4 https://www.youtube.com/watch?v=OKIfTOEo7P0
```

## 重命名

`youtube-dl` 下载的视频默认保存在当前目录，使用视频名+扩展名来保存，我们可以通过重命名的方式来修改下载目录和文件名，不过通常是在下载播放列表和频道全部视频时才需要。

是的，它还可以直接下载频道全部视频和播放列表，这样不需要写什么脚本也可以实现批量下载了

通过 `-o` 参数可以格式化下载的位置和名字

**下载播放列表**

```bash
$ youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLumqm-XDIBr1tduTDECpjF_l33IVupKAN
```

下载的文件名格式化为 `播放列表名称/视频位置 - 视频标题.扩展名`

**下载频道**

```bash
$ youtube-dl -o '%(uploader)s/%(title)s.%(ext)s' https://www.youtube.com/channel/UCahEYs3JbJQL-oyL_0H9pRA
```

下载的文件名格式化为 `上传者姓名/视频标题.扩展名`

更多的格式化模板可以看[文档](https://github.com/ytdl-org/youtube-dl#output-template)

在下载列表时有一点需要注意，很多原因都会导致下载某个视频时失败，我们希望它可以在失败跳过继续下载，而不是直接停止，加上 `-i` 参数即可。

**下载失败时跳过**

```bash
$ youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLumqm-XDIBr1tduTDECpjF_l33IVupKAN
```
