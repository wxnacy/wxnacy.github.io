---
title: Linux 环境下安装 pyenv 和 virtualenv
date: 2017-08-10
tags: [python]
---

废话不多直接上命令
## 下载
CentOS:
```bash
$ yum -y install git
$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
$ yum -y install gcc readline readline-devel readline-static openssl \
    openssl-devel openssl-static sqlite-devel bzip2-devel bzip2-libs
```
Ubuntu
```bash
$ apt-get update
$ apt-get -y install git gcc make patch zlib1g.dev libgdbm-dev libssl-dev \
    libsqlite3-dev libbz2-dev libreadline-dev
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

## 配置环境变量
vim ~/.bash_profile
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## 升级
```bash
$ pyenv update
```
## 卸载
```bash
rm -rf ~/.pyenv
然后把~/.bash_profile环境变量配置中的添加的删掉
```

