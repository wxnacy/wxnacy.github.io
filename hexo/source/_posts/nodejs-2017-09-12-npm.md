---
title: npm 使用
date: 2017-09-12
tags: [nodejs]
---


## 安装
因为 npm 是 **NodeJS** 的包管理工具，所以下载 **NodeJS** 后自动会安装 npm

<!-- more -->

### Mac
```bash
$ brew install node
```

## 命令
```bash
npm -v                      # 查看版本
sudo npm install <name> -g  # 全局安装
npm install <name>          # 本地安装
npm install <name> --save   # 本地安装，并将包信息保存到 package.json 中
npm list -g                 # 查看所有全局安装的模块
npm list <name>             # 查看某个模块的版本号
npm uninstall <name>        # 卸载模块
npm ls                      # 卸载后，你可以到 /node_modules/ 目录下查看包是否还存在
npm update <name>           # 更新模块
npm search <name>           # 搜索模块
npm init                    # 创建模块，生成 package.json
npm publish                 # 发布模块
```
