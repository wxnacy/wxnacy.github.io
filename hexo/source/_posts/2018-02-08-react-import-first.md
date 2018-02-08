---
title: React 解决 import/first 报错
tags:
  - react
date: 2018-02-08 15:59:27
---


基础错误，默写 20 遍
<!-- more -->
不管什么开发，最重要的都是基础知识啊，最近用 React 总是抱一个错误
```bash
Import in body of module; reorder to top  import/first
```
怎么也搞不清是怎么回事，今天静下心来一点点排查时，发现竟然是 `import` 没有完全写到文件最前面的关系，比如：
```javascript
import { Tabs } from 'antd';

const TabPane = Tabs.TabPane;
import 'brace/mode/css';
```
这是一个基础知识的问题，也是一个编码习惯的问题，常记于心。
