# mac 环境下安装pyenv和virtualenv虚拟机
废话不多直接上命令
## 安装pyenv
```bash
brew install pyenv
```
### 修改环境变量

```bash
$ vim ~/.bash_profile
export PYENV_ROOT="${HOME}/.pyenv"

if [ -d "${PYENV_ROOT}" ]; then
  export PATH="${PYENV_ROOT}/bin:${PATH}"
  eval "$(pyenv init -)"
fi
$ source ~/.bash_profile
```
### 查看可以安装的python版本
```bash
pyenv install —list
```
## 安装依赖
```bash
xcode-select --install brew install readline xz
brew install zlib
```
### 修改环境变量
```bash
CFLAGS="-I$(brew --prefix openssl)/include" \
LDFLAGS="-L$(brew --prefix openssl)/lib" \

```
## 安装virtualenv
```bash
brew install pyenv-virtualenv
```
### 修改环境变量
```bash
if which pyenv-virtualenv-init > /dev/null; then 
    eval "$(pyenv virtualenv-init -)"; 
fi
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
```




