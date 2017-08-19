# mac 环境下安装pyenv和virtualenv虚拟机
废话不多直接上命令
## 安装pyenv
```bash
brew install pyenv
```
### 修改环境变量

```bash
$ vim ~/.bashrc

export PYENV_ROOT="${HOME}/.pyenv"

if [ -d "${PYENV_ROOT}" ]; then
  export PATH="${PYENV_ROOT}/bin:${PATH}"
  eval "$(pyenv init -)"
fi
CFLAGS="-I$(brew --prefix openssl)/include" \
LDFLAGS="-L$(brew --prefix openssl)/lib" \

$ source ~/.bashrc # 环境变量立即生效
```

## 安装依赖
```bash
xcode-select --install
 brew install readline xz
brew install zlib
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

## 升级
```bash
brew upgrade pyenv
```

## 卸载
```bash
brew uninstall pyenv
然后删除之前填在~/.bash_profile文件里添加的内容
```




