# pyenv virtualenv 常用命令
### 查看版本列表
```bash
pyenv versions
```
### 查看当前虚拟机版本
```bash
pyenv version
```
### 查看可安装版本
```bash
pyenv install -list
```
### 安装某个版本
```bash
pyenv install -v 3.5.0
```
### 设置全局为某一个版本
```bash
pyenv global 3.5.0
```
### 创建虚拟机
```bash
pyenv virtualenv 3.5.0 env_name
```
### 本地进程使用某一版本
```bash
pyenv activate env_name
```

