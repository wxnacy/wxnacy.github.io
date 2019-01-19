---
title: 使用 electron-builder 打包 electron 程序
date: 2018-05-10 15:29:25
tags: [electron]
---

[electron-builder](https://www.electron.build/) 可以将 `electron` 程序打包为 `macOS, Linux, Windows` 三个平台的软件包，并且使用非常简单。

<!-- more --><!-- toc -->

**下载模块**

```bash
$ yarn add electron-builder --dev
```

**将配置信息添加到 `package.json` 中**

```json
"build": {
   "appId": "your.id",
   "mac": {
     "category": "your.app.category.type"
   }
 }
```

完整配置信息见[详情](https://www.electron.build/configuration/configuration#configuration)

**添加 icon**

macOS 默认使用 icon 位置为 `build/icon.icns`，更多信息见[详情](https://www.electron.build/icons)

**在 `package.json` 中添加运行脚本**

```json
"scripts": {
   "pack": "electron-builder --dir",
   "dist": "electron-builder"
 }
```

然后运行 `yarn dist` 即可打包，运行 `yarn pack` 打包后将源码打压缩包。打包目录
为 `dist`

**注意**

- 如果你的应用里面，包含有自己的原生addon (并不是依赖项)，那么请设置[nodeGypRebuild](https://www.electron.build/configuration/configuration#Configuration-nodeGypRebuild)为true。

- 如果你不是 macOS 10.12+ 系统的话，您需要安装[必须的系统包](https://electron.org.cn/builder/multi-platform-build.html)。请注意，[默认情况](https://www.electron.build/configuration/configuration#Configuration-asar)下，所有的文件都会被打包到asar压缩包中。对于一个将要马上投入生产的app，你应该对你的应用进行签名。参见[哪里可以购买签名证书](https://www.electron.build/code-signing#where-to-buy-code-signing-certificate).

你也可以将[DEMO](https://github.com/wxnacy/study/tree/master/node/electron/electron-builder)下载到本地，在 `electron-builder` 目录中执行 `yarn && yarn dist` 即可

- [electron-builder 中文](https://electron.org.cn/builder/index.html)
