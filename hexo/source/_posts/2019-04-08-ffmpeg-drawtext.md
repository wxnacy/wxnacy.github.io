---
title: Mac 系统中使用 ffmpeg 给视频添加文字水印
tags:
  - ffmpeg
date: 2019-04-08 14:16:42
---


最近有给视频加文字水印的需求，第一个想到的肯定是使用 ffmpeg，搜索了下发现网上的博客多是从别人那复制过来的，直接使用多是报错，经过摸索后，终于搞清楚了简单用法，今天简单总结下。

<!-- more --><!-- toc -->

先来看个例子，我希望在如下的视频右侧加上文字水印，如下

![mavel3](https://raw.githubusercontent.com/wxnacy/image/master/blog/mavel33.png)

## 安装

首先需要安装最新版本的 ffmpeg

```bash
$ brew install ffmpeg
```

## 英文水印

运行下面的命令，即可达到上图效果

```bash
$ ffmpeg -y -i mavel4.mp4 -vf "drawtext=text='Avengers\: Endgame':x=700:y=200:fontsize=24:fontcolor=red" mavel4_drawtext.mp4
```

参数含义
- `-i`：需要渲染的视频，`mavel4.mp4` 为视频源
- `-vf`：后面跟着需要的具体渲染效果，后面的参数需要使用双引号包裹起来
- `mavel4_drawtext.mp4`：就是最后输出的文件名
- `-y`：对一切提示回答 `yes`

`-vf` 后面的参数比较复杂，我们先将命令行折行美化下

```bash
$ ffmpeg -y -i mavel4.mp4 \
    -vf "drawtext=\
        text='Avengers\: Endgame':\
        x=700:\
        y=200:\
        fontsize=24:\
        fontcolor=red:\
        " \
    mavel4_drawtext.mp4
```

现在我们来逐条分析下

- `drawtext=`：代表了此次渲染为添加文字水印，后面跟着具体的属性，属性之间使用 `:` 分割
- `text='Avengers\: Endgame':`：想要渲染的文字内容，如果想要输入 `:`，需要使用 `\` 进行转义
- `x=700:y=200`：分别为水印距视频左侧 700 偏移量，距顶部 200 偏移量，默认为 0
- `fontsize=24:`：字体大小，默认为 16
- `fontcolor=red:`：字体颜色红色，默认为黑色

## 中文水印

这是英文的水印，不过我的需求为中文水印，我第一个反应就是乱码问题，先试一下

```bash
ffmpeg -y -i mavel4.mp4 \
    -vf "drawtext=\
        text='复仇者联盟：终局之战':\
        x=700:\
        y=200:\
        fontsize=24:\
        fontcolor=red:\
        " \
    mavel4_drawtext.mp4
```

果然，都是方块

![mavel4](https://raw.githubusercontent.com/wxnacy/image/master/blog/mavel4.png)

这是因为默认的字体文件并不支持中文，此时我们需要使用 `fontfile` 属性来制定字体文件。

网上很多博客都直接使用 `fontfile=PingFang.ttc:` 来指定文件，这多少有点误人子弟，此处应该使用字体文件的***绝对地址***。

如何获取 Mac 电脑中字体文件的绝对地址呢，请看我的的这篇文章 [Mac 电脑查看字体文件位置](/2019/04/03/mac-fonts-path/)

我选择了苹方字体，绝对地址为 `/System/Library/Fonts/PingFang.ttc`，完整命令如下

```bash
$ ffmpeg -y -i mavel4.mp4 \
    -vf "drawtext=\
        fontfile=/System/Library/Fonts/PingFang.ttc:\
        text='复仇者联盟：终局之战':\
        x=700:\
        y=200:\
        fontsize=24:\
        fontcolor=red:\
        " \
    mavel4_drawtext.mp4
```

最终渲染效果

![mavel5](https://raw.githubusercontent.com/wxnacy/image/master/blog/mavel5.png)

文字水印还有很多参数，大家可以根据自己的需求进行选择，文档地址：https://ffmpeg.org/ffmpeg-filters.html#drawtext-1
