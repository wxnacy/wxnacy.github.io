---
title: 获取 youtube 视频屏蔽地区
tags:
  - youtube
date: 2019-09-19 13:55:13
---


记得前几年 youtube 视频网页内是包含该视频的允许和屏蔽播放的区域的，但是最近需要使用时发现怎么也找不到了，估计是油管因为一些原因做了隐藏。

<!-- more -->
<!-- toc -->

先是 google 了一些方法，发现了一个网站可以查询视频的屏蔽地区，只需要输入网址或者 id 就可以了

网址：https://polsy.org.uk/stuff/ytrestrict.cgi

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/yt-polsy_1090.png)

当做网页工具还是挺不错的，对它的结果网页做解析也比较简单，但是有些视频会查询不出来，所以在程序中还是不推荐使用。

转了一圈，发现官方就有相关的 API，记得以前是有一些使用限制的，现在再找并没有发现什么限制，只有每天的调用次数限制，大概 100000 次，一般使用也足够了

网址：https://developers.google.com/youtube/v3/docs/videos

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/yt-api-videos_823.png)
