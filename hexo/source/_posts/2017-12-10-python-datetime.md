---
title: Python 时间
date: 2017-12-10 17:17:46
tags: [python]
---

在使用 Python 处理时间戳与系统时间转换时，遇到一些问题，解决后除了对问题的总结，也想把 Python 处理时间的各种情况都总结一下，慢慢更新补全，以便以后查阅

<!-- more --><!-- toc -->
## 获取时间戳
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import time
from datetime import datetime
from datetime import timezone

print(time.time())                                  # ==> 1 1512894925.029236
print(datetime.now().timestamp())                   # ==> 2 1512894925.029236
dt = datetime.utcnow()
print(dt.replace(tzinfo=timezone.utc).timestamp())  # ==> 3 1512894925.029236
```
三种方法得到的结果都是一样的，之所以列举第三种这个麻烦的方法，是因为我之前存在一个误区，认为 `datetime.utcnow().timestamp()` 得到的结果就是 Unix 时间戳，详细请见我的文章 [Python 时间戳的坑](/2017/12/05/python-timestamp-keng/)

## 时间戳转系统时间
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import time
from datetime import datetime

ts = 1512894925
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts)))
print(datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"))
```

## 系统时间转时间戳
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import time
from datetime import datetime

t = '2017-12-10 16:37:17'
print(int(time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S'))))
print(datetime.strptime(t, '%Y-%m-%d %H:%M:%S').timestamp())
```
## 时间格式化符号
- %y 两位数的年份表示（00-99）
- %Y 四位数的年份表示（000-9999）
- %m 月份（01-12）
- %d 月内中的一天（0-31）
- %H 24小时制小时数（0-23）
- %I 12小时制小时数（01-12）
- %M 分钟数（00=59）
- %S 秒（00-59）
- %f 毫秒（000-999)
- %a 本地简化星期名称
- %A 本地完整星期名称
- %b 本地简化的月份名称
- %B 本地完整的月份名称
- %c 本地相应的日期表示和时间表示
- %j 年内的一天（001-366）
- %p 本地A.M.或P.M.的等价符
- %U 一年中的星期数（00-53）星期天为星期的开始
- %w 星期（0-6），星期天为星期的开始
- %W 一年中的星期数（00-53）星期一为星期的开始
- %x 本地相应的日期表示
- %X 本地相应的时间表示
- %Z 当前时区的名称
- %% %号本身

## 使用技巧
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from datetime import date

day = date(2018, 03, 25).timetuple()
# 获取指定日期为当前星期的第几天
print(day.tm_wday + 1)  # 7
# 获取指定日期为当年的第几天
print(day.tm_yday)      # 84
```

**date/time 转为 datetime**

```python
>>> from datetime import datetime
>>> from datetime import date
>>> datetime.combine(date.today(), datetime.min.time())
datetime.datetime(2018, 4, 28, 0, 0)
```

## 参考资料
- [Python 日期和时间](http://www.runoob.com/python/python-date-time.html)
