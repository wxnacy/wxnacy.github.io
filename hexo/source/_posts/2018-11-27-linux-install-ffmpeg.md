---
title: Linux 安装 ffmpeg
date: 2018-11-27 17:30:25
tags: [linux]
---

> [ffmpeg](http://ffmpeg.org/) 是一个很强大的音视频处理工具，它是一个完整的、跨平台的解决方案，可以记录、转换和传输音频和视频。ffmpeg 既可以播放视频，也提供命令行工具来处理视频，另外还有强大的视频处理库用于开发

<!-- more --><!-- toc -->

## Ubuntu

Ubuntu 中安装比较简单，直接使用 `apt` 安装即可

```bash
$ sudo apt install -y ffmpeg
```

## CentOS

CentOS 中则比较麻烦，需要使用源码安装

**下载并解压**

```bash
$ wget https://ffmpeg.org/releases/ffmpeg-4.1.tar.bz2
$ tar -xjvf ffmpeg-4.1.tar.bz2
$ cd ffmpeg-4.1
```

**编译**

```bash
$ ./configure
nasm/yasm not found or too old. Use --disable-x86asm for a crippled build.
```

可以使用 `--disable-x86asm` 参数略过该配置或者直接安装

```bash
$ sudo yum install -y yasm
```

也可以从[官网](http://yasm.tortall.net/Download.html)下载源码安装

随后再次编译安装即可

```bash
$ ./configure
$ sudo make && sudo make install
```
