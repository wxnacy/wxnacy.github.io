---
title: Go 语法错误：relocation target main.main not defined
date: 2018-08-10 18:15:26
tags: [go]
---

> relocation target main.main not defined

<!-- more --><!-- toc -->
该错误是因为在项目中一个 `main()` 方法作为入口，在标有 `package main` 文件下添加该方法即可
