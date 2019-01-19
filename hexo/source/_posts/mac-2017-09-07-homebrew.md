---
title: Mac 包管理神器 HomeBrew
date: 2017-09-07
tags: [mac, HomeBrew]
---

> [ HomeBrew ](https://brew.sh/index_zh-cn.html) 使 macOS 更完整

<!-- more -->

<!-- toc -->

## 安装
```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

安装以后
```bash
$ echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
```
这样是让 HomeBrew 下载的包优于系统自带的包

## 使用
### 下载第一个软件包

```bash
$ brew install wget
```
这样在 Mac 中你也可以使用 wget 工具了

```bash
$ cd /usr/local
$ ls -l bin | grep 'wget'
wget -> ../Cellar/wget/1.19.1_1/bin/wget
```
通过上边一段命令，我们会发现，HomeBrew 会将软件包下载到单独的目录 /usr/local/Cellar 中，并将文件软链接到 /usr/local/bin 中

### 更多命令
```bash
$ brew install wget             # 安装包
$ brew search wget              # 搜索包（支持正则表达式）eq：brew search /^wg/
$ brew info wget                # 查看包的信息
$ brew uninstall wget           # 卸载包
$ brew switch wget 1.9.1        # 包切换到某一个版本
$ brew outdated                 # 列出过时的包
$ brew upgrade wget             # 更新包
$ brew update                   # 更新 HomeBrew 本身
$ brew cleanup wget             # 清除缓存
$ brew list                     # 列出已经安装的包
$ echo $(brew --prefix wget)    # 输出软件安装路径，/usr/local/opt/wget
```

### oh-my-zsh 补全

在安装和搜索包时，如果记不住全名可以使用 **oh-my-zsh** 的自动补全功能，但是需要下载相应的包
```bash
$ brew install zsh-completions
```

## Cask
[github](https://github.com/caskroom/homebrew-cask)

如果你已经厌倦了在新装一个机子时，到处找软件下载地址，在一个一个手动安装，那你可能需要用到 [Cask](https://caskroom.github.io/)，它可以用一条命令就安装好你需要的常规软件

### 安装
```bash
$ brew tap caskroom/cask
```

### 使用
```bash
$ brew cask install google-chrome
```
是不是很简单，赶快用起来吧

## 路径解释
- **Cellar**: 文件夹存放的是所有包安装所在路径，包括二进制，文档和配置文件，按照这样Cellar/包名/版本号/的形式来安放。
- **opt**: 由于版本号随着跟新而改变的，所以需要一个固定不变的路径作为我们访问二进制和文档的路径，这就是opt的作用。
- **Homebrew**: brew程序所在路径.
- **bin**: 所有包安装之后二进制都会链接到这个路径下
- **share**: 所有包安装之后的文档都会链接到这个路径下
- **etc**: 同上，所有包的配置文件
- **lib**: 同上，所有包相关库文件
- **Caskroom**: app文件

