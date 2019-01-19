---
title: 如何给 Hexo 博客添加 RSS 订阅功能
tags:
  - hexo
date: 2018-12-12 18:09:28
---


写这个博客有一年多了，一直都没有增加像样的订阅功能，因为觉得暂时还不会有人想专门看我的博客，也就把更多的精力放在写博客本身上了。

<!-- more --><!-- toc -->
最近收到一位网友的邮件，说希望我可以增加 RSS 订阅功能，这才想到可能有人，已经开始想更多的了解我的内容了。

那我一定是要加一下这个功能的，这样订阅功能也就加的更有目的性，更有意义了。

本篇就介绍下用 Hexo 构建的博客，如何添加 RSS 订阅功能。

首先添加功能插件，在 hexo 项目根目录下执行该命令

```bash
$ yarn add hexo-generator-feed
```

然后在 hexo 根目录下的 `_config.yml` 文件中添加配置

```bash
feed:
    type: atom
    path: atom.xml
    limit: 20
```

配置含义：
- `type`: RSS的类型(atom/rss2)
- `path`: 文件路径，默认是 atom.xml/rss2.xml
- `limit`: 展示文章的数量,使用 0 或则 false 代表展示全部
- `hub`: URL of the PubSubHubbub hubs (如果使用不到可以为空)
- `content`: （可选）设置 `true` 可以在 RSS 文件中包含文章全部内容，默认：false
- `content_limit`: （可选）摘要中使用的帖子内容的默认长度。 仅在内容设置为false且未显示自定义帖子描述时才使用。
- `content_limit_delim`: （可选）If content_limit is used to shorten post contents, only cut at the last occurrence of this delimiter before reaching the character limit. Not used by default.
- `order_by`: 订阅内容的顺序. (默认: -date)
（后面几个选项一般用不到，有两个也没找到比较准确的翻译，所以感觉放上原文，如果你知道一定要告诉我）

然后在 theme 目录下的 `_config.yml` 文件中添加配置

```bash
rss: /atom.xml
```

随后重新生成博客静态文件

```bash
$ hexo clean && hexo g
```

在 `public` 文件夹中就会生成 `atom.xml` 文件，部署后直接在根目录中访问该文件即可

```bash
https://wxnacy.com/atom.xml
```

我使用的是 yilia 皮肤，在 `_config.yml` 中添加配置

```bash
subnav:
    rss: "atom.xml"
```

即可在导航栏生成 RSS 图标

![rss](/images/rss.png)
