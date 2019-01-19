---
title: Yarn 简单使用
date: 2018-05-13 21:19:55
tags: [node]
---

yarn 的简单使用。

<!-- more --><!-- toc -->
## 初始化新项目

```bash
yarn init
```

## 添加依赖包

```bash
yarn add [package]
yarn add [package]@[version]
yarn add [package]@[tag]
```

## 将依赖项添加到不同依赖项类别

分别添加到 devDependencies、peerDependencies 和 optionalDependencies：

```bash
yarn add [package] --dev
yarn add [package] --peer
yarn add [package] --optional
```

## 升级依赖包

```bash
yarn upgrade [package]
yarn upgrade [package]@[version]
yarn upgrade [package]@[tag]
```

## 移除依赖包

```bash
yarn remove [package]
```

## 安装项目的全部依赖

```bash
yarn
```

或者

```bash
yarn install
```

- [yarn 使用](https://yarnpkg.com/zh-Hans/docs/usage)
