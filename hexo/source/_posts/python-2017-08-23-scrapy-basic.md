---
title: Python Scrapy 入门教程
date: 2017-08-23
tags: [python]
---


## 安装
```bash
$ pip install Scrapy
```

## 创建项目
```bash
$ scrapy startproject crawler

New Scrapy project 'crawler', using template directory '/Users/wxnacy/.pyenv/versions/3.5.0/envs/env_lightcircle/lib/python3.5/site-packages/scrapy/templates/project', created in:
    /Users/wxnacy/WebstormProjects/wxnacy.github.io/crawler

You can start your first spider with:
    cd crawler
    scrapy genspider example example.com

```

通过提示我们可以通过如下命令创建第一个spider
```bash
$ cd crawler
$ scrapy genspider youtube youtube.com

Created spider 'youtube' using template 'basic' in module:
  crawler.spiders.youtube

```