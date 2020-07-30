---
title: 计算两个经纬度之间的直线距离
date: 2017-12-05 17:45:16
tags: [算法, python, javascript]
---

在针对经纬度之间距离的运算维基百科推荐使用 [Haversine](https://en.wikipedia.org/wiki/Haversine_formula) 算法

<!-- more -->
<!-- toc -->

## Python

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from math import radians, cos, sin, asin, sqrt

def distance_between_points(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(
            radians, [float(lon1), float(lat1), float(lon2), float(lat2)])
    # haversine 公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000     # 结果单位米

if __name__ == '__main__':
    location = (39.7836455948, 116.5627747582, 39.7833570280, 116.5636974381)
    print(distance_between_points(*location))   # ==> 85.12205329599756
    ```

## Javascript

```javascript
rad = function(x) {return x*Math.PI/180;}

distHaversine = function(p1, p2) {
    var R = 6371; // earth's mean radius in km
    var dLat  = rad(p2.lat() - p1.lat());
    var dLong = rad(p2.lng() - p1.lng());

    var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
        Math.cos(rad(p1.lat())) * Math.cos(rad(p2.lat())) *
        Math.sin(dLong/2) * Math.sin(dLong/2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    var d = R * c;

    return d.toFixed(3);

}
```

## Excel

```bash
# C2, D2 = lat1, lng1
# F2, G2 = lat2, lng2
=6371004*SQRT(POWER(COS(C2*PI()/180)*(G2*PI()/180-D2*PI()/180),2)+POWER((F2*PI()/180-C2*PI()/180),2))
```

## 参考

- [Calculate distance, bearing and more between Latitude/Longitude points](http://www.movable-type.co.uk/scripts/latlong.html)
