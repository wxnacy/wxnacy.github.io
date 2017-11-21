---
title: pyenv 常用命令
date: 2017-08-10
tags: [python]
---

## pyenv
### 查看可安装版本
```bash
pyenv install -list
```
### 安装某个版本
```bash
pyenv install -v 3.5.0
```
### 查看本地版本列表
```bash
$ pyenv versions

* system (set by /home/wxnacy/.pyenv/version) # 系统python环境 *号代表当前环境版本
  3.5.0 # 刚下载的3.5.0版本
```
### 查看当前环境版本
```bash
$ pyenv version
system (set by /home/wxnacy/.pyenv/version)
```

### 设置全局为某一个环境
```bash
$ pyenv global 3.5.0
$ pyenv version # 查看当前环境
3.5.0 (set by /home/wxnacy/project/project_350/.python-version)
```


### 为项目设置单独环境
```bash
$ cd project
$ pyenv local 3.5.0 # 使用local命令为某个目录单独设置目录
$ pyenv version
3.5.0 (set by /home/wxnacy/project/project_350/.python-version)

$ cd ..
$ pyenv version # 退出目录查看环境没有改变
system (set by /home/wxnacy/.pyenv/version)
```



## virtualenv
假如我们有多个项目都是用3.5.0的环境，但是又不想让他们公用一个环境该怎么办？
使用virtualenv可以为某一个python版本创建一个干净的虚拟机环境
### 创建虚拟机
```bash
$ pyenv virtualenv 3.5.0 env_350
$ pyenv versions
* system (set by /home/wxnacy/.pyenv/version)
  3.5.0
  3.5.0/envs/env_350
  env_350
```
查看环境后我们发现多了两个环境`3.5.0/envs/env_350`和`env_350`，这两个是同一个
### 指定当前进程环境
```bash
pyenv activate env_350
```
该命令只能指定当前进程的环境，退出shell后重新进入，发现环境又变回之前的环境
### 当前进行退出activate

```bash
$ pynev deactivate
```
当然virtualenv生成的虚拟环境也可以配合`global`和`local`等pyenv命令配合使用

