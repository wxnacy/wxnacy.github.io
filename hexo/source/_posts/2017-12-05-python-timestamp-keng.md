---
title: Python 时间戳的坑
date: 2017-12-05 17:23:36
tags: [python]
---
在使用 `datetime` 的 `timestamp()` 方法获取时间戳时遇到一点问题
<!-- more -->

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from datetime import datetime
print(datetime.now().timestamp()        # ==> 1512393482.510263
print(datetime.utcnow().timestamp())    # ==> 1512364682.510288
```
理论上两个输出应该都返回当前时间戳，但是 `utcnow()` 方法的时间戳并不正确，网上查找资料没一个能说明白的，后来查看[官方文档](https://docs.python.org/dev/library/datetime.html#datetime.datetime.timestamp)发现这么一句话
> There is no method to obtain the POSIX timestamp directly from a naive datetime instance representing UTC time. If your application uses this convention and your system timezone is not set to UTC, you can obtain the POSIX timestamp by supplying tzinfo=timezone.utc:

我们不能通过 UTC 得到的 `datetime` 实例直接获取时间戳，如果系统的时区不是 UTC 则需要 `timezone.utc` 来帮忙转换。我晕，我们不提供，但是给你指条路。好吧，先试试
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from datetime import datetime
from datetime import timezone

dt = datetime.utcnow()
print(dt.replace(tzinfo=timezone.utc).timestamp())  # ==> 1512454062.906826
print(datetime.now().timestamp())                   # ==> 1512454062.906826
```

OK，这次可以了，但是呢，难道每次获取一次时间戳都这样麻烦或者修改系统时区吗？当然不是，我们还可以通过 `time` 模块来轻松搞定
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import time

print(time.time())      # ==> 1512454270.614852
```

## 时间戳转为地区时间
如果想要将时间戳转为某个地区的时间，比如北京时间，需要引入 `pytz` 模块，首先下载 `pip install pytz`
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import time
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Shanghai') #东八区
t = datetime.fromtimestamp(int(time.time()),
    pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
print(t)    # ==> 2017-12-05 18:39:45 CST+0800
```

