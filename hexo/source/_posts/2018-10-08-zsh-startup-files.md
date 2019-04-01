---
title: Zsh 配置文件加载顺序
date: 2018-10-08 15:33:42
tags: [zsh]
---

Zsh 中我们最常用到的配置文件为 `~/.zshrc`，但其实它完整的生命周期还有很多配置文件。

<!-- more -->

它们是

```bash
/etc/zshenv
/etc/zprofile
/etc/zshrc
/etc/zlogin
/etc/zlogout
~/.zshenv
~/.zprofile
~/.zshrc
~/.zlogin
~/.zlogout
```

它们的加载顺序为

```bash
/etc/zshenv
~/.zshenv
/etc/zprofile
~/.zprofile
/etc/zshrc
~/.zshrc
/etc/zlogin
~/.zlogin
~/.zlogout
/etc/zlogout
```

`/etc` 下的配置文件我们通常不会去修改，我们更关心当前用户的 Zsh 生命周期。

我们可以分别在 `~/.zshenv` `~/.zprofile` `~/.zshrc` `~/.zlogin` `~/.zlogout` 中添加相应名字的打印信息，比如：

```bash
echo '.zshrc' >> /tmp/zsh_startups
```

我们先打开一个 Terminal 监听该文件的变化

```bash
$ tail -f /tmp/zsh_startups
```

然后再打开一个 Terminal，可以看到日志变化

```bash
.zshenv
.zprofile
.zshrc
.zlogin
```

当关闭该 Terminal，则会在打印一次 `~/.zlogout`

这次我们打开 Terminal 后，重新切换 Zsh 环境

```bash
$ zsh
```

这次的加载顺序为

```bash
.zshenv
.zshrc
```

从这里我们可以得知，打开新的 Terminal 和切换 Zsh 配置的加载区别。

这样我们可以得到一个信息，那就是把耗时长，并且不经常变动的的配置信息放到 `~/.zprofile` 中，这样大部分的耗时只发生在打开 Terminal 时，从而提高执行 `source ~/.zshrc` 的速度。

- [Startup/Shutdown Files](http://zsh.sourceforge.net/Doc/Release/Files.html#Startup_002fShutdown-Files)
