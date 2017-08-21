# linux 环境下安装pyenv和virtualenv虚拟机
废话不多直接上命令
## 下载
CentOS:
```bash
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```
Ubuntu
```bash
apt-get -y install git gcc make patch zlib1g.dev libgdbm-dev libssl-dev libsqlite3-dev libbz2-dev libreadline-dev
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
## 安装依赖
```bash
sudo yum install readline readline-devel readline-static
sudo yum install openssl openssl-devel openssl-static
sudo yum install sqlite-devel
sudo yum install bzip2-devel bzip2-libs
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

