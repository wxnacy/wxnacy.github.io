---
title: Hexo 如何引入自定义 js 文件
date: 2017-12-12 18:08:29
tags: [hexo]
---

在写 [获取时间戳及世界时间转换](/2017/12/09/timestamp/) 和 [如何获取指定位数随机数](/2017/12/06/get-random/) 两篇文章的时候，因为文中出现一些工具性质的东西，需要 js 代码的运算，但是又不能都写到 markdown 文件中，所以需要在 Hexo 中引入静态 js 文件。
<!-- more -->

在查阅文档后发现 Hexo 中静态文件放在皮肤文件夹中，即
```bash
your_project/themes/<theme_name>/source
```
在这个文件夹中会有 `js, css, img` 等文件夹，没有的话可以自己创建，将自定义的 js 放到其中，在 markdown 文章中直接引用即可
```javascript
<script type="text/javascript" src="/js/test.js"></script>
```

