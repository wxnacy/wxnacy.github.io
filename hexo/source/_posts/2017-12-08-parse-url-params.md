---
title: 如何解析地址参数
date: 2017-12-08 13:48:12
tags: [算法, javascript, java, python]
---

在 React 之前 html 页面想要获取当前地址参数，只能通过静态解析的方式在获取，列举几种语言的获取方式

<!-- more --><!-- toc -->
## Javascript
```javascript
function getValue(key) {
    var name = key + "=";
    var str = window.location.search;
    var beginIndex = str.indexOf("?" + name);
    if (beginIndex == -1) {
        beginIndex = str.indexOf("&" + name);
    }
    if (beginIndex != -1) {
        var pos_start = beginIndex + name.length + 1;
        var pos_end = str.indexOf("&", pos_start);
        if (pos_end == -1) {
            return decodeURIComponent(str.substring(pos_start));
        } else {
            return decodeURIComponent(str.substring(pos_start, pos_end));
        }
    }
}
```

## Python
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def get_value(url, k):
    """获取地址中参数值"""
    nk = '{}='.format(k)
    if nk not in url:
        return None

    b = url.find(nk) + len(nk)  # 获取开始位置
    e = url.find('&', b) if url.find('&', b) != -1 else len(url)    # 结束位置
    v = url[b:e]
    return v
```

## Java
```java
public static String getValue(String url, String key){
    String k = key + "=";
    int begin = url.indexOf(k);
    if(begin == -1){
        return null;
    }
    begin = begin + k.length();
    int end = url.indexOf("&", begin);
    if(end == -1){
        return url.substring(begin);
    }else {
        return url.substring(begin, end);
    }
}
```
