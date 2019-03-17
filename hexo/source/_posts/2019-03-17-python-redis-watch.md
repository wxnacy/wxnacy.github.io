---
title: Python 使用 Redis watch 完成秒杀活动防止超卖 demo
tags:
  - python
  - redis
date: 2019-03-17 10:49:48
---


在做类似抢购活动的程序，我们通常会使用“乐观锁”思路，既保证库存不会超卖，也能够应付大并发的情况，Redis 中 watch 就可以实现“乐观锁”。

<!-- more --><!-- toc -->

Redis 中的事务 `multi/exec` 可以保证数据的原子性，但不能像 Mysql 那样在事务中出错回滚数据，而用 `watch` 来监听数据，就可以实现类似的功能。

先用 `watch` 监听后，在接下来事务的过程，如果数据被修改，则在执行 `exec` 时，则会报错，我们可以根据业务选择重试和返回结果。

Python 中通过管道 Pipeline 来实现 Redis 事务相关操作。

**初始化线程池**

```python
import redis

# 创建连接池
pool = redis.ConnectionPool(host = '127.0.0.1', port=6379, db=0)
# 初始化 redis
r = redis.Redis(connection_pool = pool)
```

**初始化管道**

```python
pipe = r.pipeline()
```

**使用事务**

```python
KEY = 'count'
try:
    pipe.watch(KEY)         # 监听库存
    pipe.multi()            # 开始事务
    pipe.set(KEY, 2)        # 执行操作
    pipe.execute()          # 执行事务
except Exception as e:
    # 事务执行过程中，如果数据被修改，则抛出异常，程序可以选择重试或退出
    pass
finally:
    pipe.reset()            # 重置管道，为重试做准备
```

通过这些操作，我们可以先实现一个防止商品超卖的 demo。

代码位置 [watch_demo.py](https://github.com/wxnacy/study/blob/master/python/redis_demo/watch_demo.py)

**运行**

```bash
$ python watch_demo.py
用户 0 抢购成功，商品剩余 9
用户 1 抢购成功，商品剩余 8
用户 2 抢购失败，重试一次
用户 3 抢购成功，商品剩余 7
用户 5 抢购失败，重试一次
用户 4 抢购失败，重试一次
用户 2 抢购失败，重试一次
用户 6 抢购失败，重试一次
用户 7 抢购失败，重试一次
用户 9 抢购失败，重试一次
用户 8 抢购成功，商品剩余 6
用户 10 抢购成功，商品剩余 5
用户 5 抢购成功，商品剩余 4
用户 12 抢购失败，重试一次
用户 6 抢购失败，重试一次
用户 13 抢购成功，商品剩余 3
用户 11 抢购失败，重试一次
用户 14 抢购失败，重试一次
用户 2 抢购失败，重试一次
用户 4 抢购失败，重试一次
用户 9 抢购成功，商品剩余 2
用户 7 抢购失败，重试一次
用户 12 抢购成功，商品剩余 1
用户 2 抢购停止，商品卖完
用户 6 抢购失败，重试一次
用户 14 抢购失败，重试一次
用户 4 抢购停止，商品卖完
用户 11 抢购成功，商品剩余 0
用户 7 抢购停止，商品卖完
用户 6 抢购停止，商品卖完
用户 14 抢购停止，商品卖完
```
