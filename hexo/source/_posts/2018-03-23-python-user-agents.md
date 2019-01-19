---
title: Python User Agents
tags:
  - python
date: 2018-03-23 15:29:04
---


最近在写流量监控，需要分析 User Agent，写了两行，放弃，我为什么不找个工具干这事。

<!-- more --><!-- toc -->
`user_agents` 是 Python 库，可以解析用户代理中使用系统、设备、浏览器等信息。它依赖于 `ua_parse` 解析库对原始代理字符串的解析。
## 下载
```bash
pip install pyyaml ua-parser user-agents
```
## 设备信息
系浏览、器统、设备
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from user_agents import parse

# iPhone's user agent string
ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
user_agent = parse(ua_string)

# Accessing user agent's browser attributes
user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
user_agent.browser.family  # returns 'Mobile Safari'
user_agent.browser.version  # returns (5, 1)
user_agent.browser.version_string   # returns '5.1'

# Accessing user agent's operating system properties
user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
user_agent.os.family  # returns 'iOS'
user_agent.os.version  # returns (5, 1)
user_agent.os.version_string  # returns '5.1'

# Accessing user agent's device properties
user_agent.device  # returns Device(family=u'iPhone', brand=u'Apple', model=u'iPhone')
user_agent.device.family  # returns 'iPhone'
user_agent.device.brand # returns 'Apple'
user_agent.device.model # returns 'iPhone'

# Viewing a pretty string version
str(user_agent) # returns "iPhone / iOS 5.1 / Mobile Safari 5.1"
```

## 设备类型判断
- `is_mobile` 是否为手机
- `is_pc` 是否为桌面电脑
- `is_tablet` 是否为平板设备
- `is_touch_capable` 是否为触摸设备
- `is_bot` 是否为爬虫机器人

- [Python User Agents](https://github.com/selwin/python-user-agents)
