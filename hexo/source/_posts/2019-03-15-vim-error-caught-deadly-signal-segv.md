---
title: Vim 报错：Caught deadly signal SEGV
date: 2019-03-15 10:15:35
tags: [vim]
---

Mac 系统大版本的升级总是会引来一些灾难，这次升级到 macOS Mojave 就有很多软件都用不了了，Vim 就是其中一个。

<!-- more --><!-- toc -->

```bash
Vim: Caught deadly signal SEGV
Error detected while processing function 81_PollServerReady[7]..81_Pyeval:Vim: Finished.

line 4:
Exception MemoryError: MemoryError() in <module 'threading' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.pyc'> ignored
```

这不，每次启动都报这个错误，然后闪退程序。这就很尴尬了，我现在的开发工作都是在 Vim 中进行，用不了可咋整，网上的说法是因为 YouCompleteMe 插件导致的，需要重新安装 Vim 并使之支持 lua。

我使用 `vim --version` 查看，发现果然当前不支持

```bash
$ vim --version
...
-lua
...
```

按照网上教程安装

```bash
$ brew install vim --with-lua --with-override-system-vi
...
Error: invalid option: --with-lua
```

结果报错，无效的参数？？？但是翻遍了 Google 给出的都是这个教程，继续搜索，发现现在新版本的 brew 认为 `--` 会让使用者困惑，所以慢慢去掉了这些参数，去的真及时，那你倒是把新的方法贴出来啊。

我只能暂时退而求其次把 YouCompleteMe 插件删掉好了，结果果然正常了，反正是能用了，就是补全功能差劲点，别扭点就别扭点吧，还要工作呢。

勉强用了一天，觉得还是不行，已经被 YouCompleteMe 惯出毛病了，转了一圈，发现只输入点后自动提示补全和写入文字自动补全时忽略大小写这两点，就没有一个插件可以代替，无奈还是要想办法解决这个问题。

既然 brew 不能带这些参数，那去掉试试好了。

```bash
$ brew install vim
```

再次运行 `vim` 还是不行，我试着查看了下 vim 的位置

```bash
$ which vim
/usr/bin/vim
```

隐约觉得事情不太对，通常 brew 安装的软件二进制文件是在 `/usr/local/bin` 中的，查看了下发现果然没有链接过去，再次链接

```bash
$ sudo chown $(whoami):wheel /usr/local/share/man/de/man1
$ brew link vim
```

再次查看

```bash
$ which vim
/usr/bin/vim
```

还是不行，查看环境变量发现 `$PATH` 中，`/usr/bin` 靠后，会覆盖的 `/usr/local/bin` 中的命令，再次调整

```bash
$ vim .bash_profile
export $PATH=$PATH:/usr/local/bin
$ source .bash_profile
```

再次查看

```bash
$ which vim
/usr/local/bin/vim
```

搞定，查看版本

```bash
$ vim --version
...
+lua
...
```

好像有戏了，我怀着忐忑的心情，再次安装上 YouCompleteMe，打开 Vim，一切正常。

![vim](https://wxnacy-img.oss-cn-beijing.aliyuncs.com/blog/vim1_1440_720.png)

***有些时候就是这样，事情总会得到解决，我们可以逃避过去，也可以休息一下，然后重新挑战。***

- [#3165](https://github.com/Valloric/YouCompleteMe/issues/3165)
- [brew - Error: invalid option](https://blog.csdn.net/weixin_39569611/article/details/87278729)
