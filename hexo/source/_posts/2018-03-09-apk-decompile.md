---
title: Mac 上反编译 Android APK
tags:
  - mac
  - 工具
date: 2018-03-09 11:26:24
---


最近在对一款 app 软件进行抓包，但是接口的返回数据是加密的，没办法只能试着反编译 apk，然后分析它的代码，当然我是抱着学习的心态来进行如下操作的

<!-- more --><!-- toc -->
## 条件
- JDK 7 及以上
- demo.apk 想要反编译的 apk
- Apktool 工具
- dex2jar
- JD-GUI

## Apktool
JDK 就不再说了，如果不知道怎么装，请移步google

首先安装 [Apktool](https://ibotpeaches.github.io/Apktool/install/) 环境，这是反编译的基础，接下跟紧我的脚步

下载 Apktool 命令脚本
```bash
$ wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/osx/apktool
$ chmod +x apktool
$ mv apktool /usr/local/bin
```
这里需要注意名字不要加上 `.sh` 后缀，然后从 https://bitbucket.org/iBotPeaches/apktool/downloads/ 下载最新的 jar 包
```bash
$ mv apktool_x.x.x.jar apktool.jar
$ chmod +x apktool.jar
$ mv apktool.jar /usr/local/bin
$ apktool --version
2.3.1
```
这样我们就安装好了 Apktool，下面我们来测试下反编译和编译是否能成功
```bash
$ apktool d demo.apk

I: Using Apktool 2.3.1 on sp.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
S: WARNING: Could not write to (/Users/wxnacy/Library/apktool/framework), using /var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/ instead...
S: Please be aware this is a volatile directory and frameworks could go missing, please utilize --frame-path if the default storage directory is unavailable
I: Loading resource table from file: /var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```
运行命令后，如果出现上述类似信息，并在当前目录下生成一个 demo 文件夹，代表反编译成功了，文件夹内就是反编译后的内容

也可以将文件夹反编译为 apk
```bash
$ apktool b demo

I: Using Apktool 2.3.1
I: Checking whether sources has changed...
I: Smaling smali folder into classes.dex...
I: Checking whether resources has changed...
I: Building resources...
S: WARNING: Could not write to (/Users/wxnacy/Library/apktool/framework), using /var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/ instead...
S: Please be aware this is a volatile directory and frameworks could go missing, please utilize --frame-path if the default storage directory is unavailable
I: Copying libs... (/lib)
I: Building apk file...
```
在 demo 文件夹中生成 `build, dist` 两个文件夹，这就是编译后生成的文件，apk 在 dist 中

## dex2jar
接下来我们需要使用 dex2jar 将 apk 转为 jar 文件，首先从网址 https://github.com/pxb1988/dex2jar/releases 下载最新版的 dex2jar，并解压到 dex2jar 文件夹
```bash
$ cd dex2jar
# 添加执行权限
$ chmod +x d2j_invoke.sh
$ chmod +x d2j-dex2jar.sh
$ ./d2j-dex2jar.sh ~/demo.apk
```
随后会在当前目录得到 demo-dex2jar.jar 文件

## JD-GUI
最后就剩打开源码了，从 http://jd.benow.ca/ 中下载最新的 jar 文件，在电脑上打开这个文件会启动一个 jar 客户端，并将生成的 demo-dex2jar.jar 拖入其中即可
![/images/uncomplete.png](/images/uncomplete.png)
