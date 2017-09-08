# zsh 与 oh-my-zsh 安装与使用

[TOC]

## 安装 zsh
### Linux
```bash
$ yum install zsh
$ chsh -s /bin/zsh # 将默认shell改为zsh
$ echo $SHELL # 查看是否生效
```
### Mac
```bash
$ brew install zsh

$ which zsh
/usr/local/bin/zsh  # 执行which命令发现brew将zsh安装到了/usr/local/bin/zsh

# 所以首先需要将zsh执行脚本所在位置写入到/etc/shells 中，在进行chsh操作
$ sudo vim /etc/shells

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


# 保存退出后在更换shell
$ chsh -s /usr/local/bin/zsh
$ echo $SHELL # 查看是否生效

```

## 安装 [ oh-my-zsh ](http://ohmyz.sh/)


curl
```bash
$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
wget
```bash
$ sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

最后修改zshrc兼容bash_profile的环境变量
```bash
$ vim ~/.zshrc
$ source ~/.bash_profile
```

## 皮肤

```bash
$ vim ~/.zshrc

...
ZSH_THEME="fishy"       # 修改此处可以更改zsh使用皮肤
...
```

[更多皮肤](https://github.com/robbyrussell/oh-my-zsh/wiki/themes)
