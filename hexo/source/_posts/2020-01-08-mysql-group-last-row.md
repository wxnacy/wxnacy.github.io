---
title: Mysql 分组查找最后一条记录
date: 2020-01-08 16:45:19
tags: [mysql]
---

现在有一张表，以 `yt_channel_id` 为外键 id，不断的写进数据，每次的数据 `videos` 字段会不一样。

<!-- more -->
<!-- toc -->

现在想要批量每个 `yt_channel_id` 最新插入的数据，使用 `group` 配合 `max(create_ts)` 即可。

```mysql
$ select yt_channel_id, videos, max(create_ts) from youtube_data group by yt_channel_id;
```

不过 `5.7.19` 版本不可用，直接报错，`5.7.23` 及以上可用。
