---
title: test
tags:
---

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def get_value(url, k):
    """获取地址中参数值"""
    nk = '{}='.format(k)
    if nk in url:
        b = url.find(nk) + len(nk)
        e = url.find('&', b) if url.find('&', b) != -1 else len(url)
        v = url[b:e]
        return v
    return None
```
```javascript
funtion getValue (key) {
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
