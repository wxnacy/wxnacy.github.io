---
title: Zsh 与 oh-my-zsh 安装与使用
date: 2017-08-16
tags: [linux, mac]
---

经常操作 Unix 系统有一款好的 Shell 工具是必备的，程序员刚开始接触的都是 Bash
随着时代的进步，有越来越多的更好更方便的 Shell 工具可用，下面我们来介绍里面的
翘楚 ***Zsh***

<!-- toc -->

## 安装 Zsh
### CentOS
```bash
$ yum -y install zsh
```
### Ubuntu
```bash
$ apt-get -y install zsh
```
### Mac
```bash
$ brew install zsh
```

安装完毕我们就可以通过输入 `zsh` 进入 Zsh 命令行，如果想系统默认使用 Zsh 则可以
修改配置文件
```bash
$ chsh -s /bin/zsh # 将默认shell改为zsh
$ echo $SHELL # 查看是否生效
```
但是在 Mac 系统中这样会失败，因为 Zsh 的默认位置不在 `/bin/zsh`
```bash
$ which zsh
/usr/local/bin/zsh
```
通过如上命令可以发现，brew 将 Zsh 安装到到 `/usr/local/bin/zsh`
我们需要修改 Shell 配置，`sudo vim /etc/shells`
```bash
# List of acceptable shells for chpass(1).
  2 # Ftpd will not allow users to connect who are not using
  3 # one of these shells.
  4
  5 /bin/bash
  6 /bin/csh
  7 /bin/ksh
  8 /bin/sh
  9 /bin/tcsh
-10 /bin/zsh
+10 /usr/local/bin/zsh
```
我们将新的 Zsh 位置替换掉以前的，关闭文件，再次执行开始的命令即可

## 安装 oh-my-zsh
想要更好的使用 Zsh 我们还需要安装一个配置管理工具 [oh-my-zsh](http://ohmyz.sh/)
curl
```bash
$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
wget
```bash
$ sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

最后修改配置兼容 bash_profile 的环境变量 `vim ~/.zshrc`
```bash
...
source ~/.bash_profile
...
```

## 皮肤

```bash
修改配置文件 `vim ~/.zshrc`

...
ZSH_THEME="fishy"       # 修改此处可以更改zsh使用皮肤
...
```

[更多皮肤](https://github.com/robbyrussell/oh-my-zsh/wiki/themes)

Zsh 可以支持一些第三方应用命令的快速输入或简写，比如 `gst` 直接对应 `git status`
`gd` 对应 `git diff`，这样在开发或维护服务都很有效率，不过想要生效还需要配置一下
`vim ~/.zshrc`
```bash
...
plugins=(git)
...
```
