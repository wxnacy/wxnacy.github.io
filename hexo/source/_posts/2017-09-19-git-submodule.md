---
title: Git 工具 submodule
date: 2017-09-19 22:14:07
tags: [git]
---

> Git submodule 是一个很好的多项目使用共同类库的工具，他允许类库项目做为repository,子项目做为一个单独的 Git 项目存在父项目中，子项目可以有自己的独立的commit，push，pull。而父项目以Submodule的形式包含子项目，父项目可以指定子项目header，父项目中会的提交信息包含Submodule的信息，再clone父项目的时候可以把Submodule初始化。

<!-- more -->
添加
```bash
$ git submodule add https://github.com/chaconinc/DbConnector
```

通过 `git status` 查看状态
```bash
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   .gitmodules
	new file:   DbConnector
```

此时项目中增加一个 ***.gitmodules*** 文件
```bash
$ cat .gitmodules
[submodule "DbConnector"]
	path = DbConnector
	url = https://github.com/chaconinc/DbConnector
```
增加一个模块，该文件就会增加一条记录。
该文件也会受到版本控制，这样项目就知道从哪里获取子模块

## 克隆含有子模块的项目
接下来我们将会克隆一个含有子模块的项目。 当你在克隆这样的项目时，默认会包含该子模块目录，但其中还没有任何文件：
```bash
$ git clone https://github.com/chaconinc/MainProject
```
现在 DbConnector 目录是空的，只有执行如下两个命令才可以
```bash
$ git submodule init
$ git submodule update
```
或者
```bash
$ git submodule update --init --recursive
```
不过还有更简单一点的方式。 如果给 `git clone` 命令传递 `--recursive` 选项，它就会自动初始化并更新仓库中的每一个子模块。
```bash
$ git clone --recursive https://github.com/chaconinc/MainProject
```

## 删除子模块
想要删除子模块需要进行两部操作
```bash
$ rm -rf DbConnector/
$ git rm DbConnector/
```
此时想要重新添加该子模块可能会报 ***'DbConnector' already exists in the index*** 的错误，此时我们需要加上 `--force` 参数
```bash
$ git submodule add --force https://github.com/chaconinc/DbConnector
```

## 参考文献
- [Git 工具 - 子模块](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97)
