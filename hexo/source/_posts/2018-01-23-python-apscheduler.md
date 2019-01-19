---
title: Python APScheduler 定时任务
tags:
  - python
date: 2018-01-23 18:30:32
---


APScheduler 是 Python 一个定时任务框架，可以指定日期、固定时间间隔等任务。

<!-- more --><!-- toc -->
## 下载
```bash
$ pip install apscheduler
```
## Hello World
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

sched = BlockingScheduler()

def my_job():
    print(f'{datetime.now():%H:%M:%S} Hello World ')

sched.add_job(my_job, 'interval', seconds=5)
sched.start()
```
```bash
17:17:05 Hello World
17:17:10 Hello World
17:17:15 Hello World
17:17:20 Hello World
17:17:25 Hello World
17:17:30 Hello World
```
APScheduler 使用起来非常简单，上面的代码完成了每个五秒输出一次信息的功能，它通过如下几个步骤是实现
- `BlockingScheduler` 调度器中的一种，该种表示在进程中只运行调度程序时使用。
- `sched.add_job()` 添加作业，并指定调度方式为 `interval`，时间间隔为 5 秒
- `sched.start()` 开始任务

除了上述添加作业的方法，还可以使用装饰器
```python
@sched.scheduled_job('interval', seconds=5)
def my_job():
    print(f'{datetime.now():%H:%M:%S} Hello World ')
```
如果同一个方法被添加到多个任务重，则需要指定任务 id
```python
@sched.scheduled_job('interval', id='my_job', seconds=5)
@sched.scheduled_job('interval', id='my_job1', seconds=3)
def my_job():
    print(f'{datetime.now():%H:%M:%S} Hello World ')
```

## 调度器
除了刚才用到的调度器，总共有如下几种
- `BlockingScheduler` 进程中只运行调度程序时使用。
- `BackgroundScheduler` 当没有使用任何框架时使用，并希望调度程序在应用程序的后台运行。
- `AsyncIOScheduler` 当应用程序使用 `asyncio` 模块时使用
- `GeventScheduler` 当应用程序使用 `gevent` 时使用
- `TornadoScheduler` 当创建 `Tornado` 应用时使用
- `TwistedScheduler` 当创建 `Twisted` 应用时使用
- `QtScheduler` 当创建 `Qt` 应用时使用
比较常用的是前两个

## 调用方式
`add_job()` 中 `trigger` 参数为调用方式，有 `interval, day, cron` 三种值
### cron
指定时间调度，参数如下
- year (int|str) – 4-digit year
- month (int|str) – month (1-12)
- day (int|str) – day of the (1-31)
- week (int|str) – ISO week (1-53)
- day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
- hour (int|str) – hour (0-23)
- minute (int|str) – minute (0-59)
- second (int|str) – second (0-59)
- start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
- end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
- timezone (datetime.tzinfo|str) – time zone to use forthe date/time calculations (defaults to scheduler timezone)
- jitter (int|None) – advance or delay the job execution by jitter seconds at most.

当参数指定字符串时有许多种用法，比如：
```python
# 当前任务会在 6、7、8、11、12 月的第三个周五的 0、1、2、3 点执行
sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
```

更多的用法见[文档](http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html#expression-types)

### interval
时间间隔调用，参数如下
- weeks (int) – number of weeks to wait
- days (int) – number of days to wait
- hours (int) – number of hours to wait
- minutes (int) – number of minutes to wait
- seconds (int) – number of seconds to wait
- start_date (datetime|str) – starting point for(int i = 0; i < the interval calculation
- end_date (datetime|str) – latest possible date/time to trigger on
- timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations
- jitter (int|None) – advance or delay the job execution by jitter seconds at most.

假如你要做一个活动，定时任务需要指定一个时间区间，就不需要手动去开启或停止了，只需要像下边这样设置 `start_date, end_date` 即可
```python
sched.add_job(job_function, 'interval', hours=2, start_date='2018-01-10 09:30:00', end_date='2018-06-15 11:00:00')
```
更多的用法见[文档](http://apscheduler.readthedocs.io/en/latest/modules/triggers/interval.html#examples)

### date
指定时间，但只会执行一次
- run_date (datetime|str) – the date/time to run the job at
- timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already

例子
```python
@sched.scheduled_job('date', id='my_job', run_date='2018-01-23 18:25:30')
```
更多的用法见[文档](http://apscheduler.readthedocs.io/en/latest/modules/triggers/date.html)

## 参考
- [Advanced Python Scheduler](http://apscheduler.readthedocs.io/en/latest/index.html)
- [Python任务调度模块 – APScheduler](http://debugo.com/apscheduler/)
