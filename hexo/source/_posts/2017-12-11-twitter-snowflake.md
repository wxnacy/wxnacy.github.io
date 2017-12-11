---
title: Twitter Snowflask 64位自增id算法几个语言实现方法
date: 2017-12-11 18:33:16
tags: [算法, python]
---
> [Twitter-Snowflake](https://github.com/twitter/snowflake) 算法产生的背景相当简单，为了满足Twitter每秒上万条消息的请求，每条消息都必须分配一条唯一的id，这些id还需要一些大致的顺序（方便客户端排序），并且在分布式系统中不同机器产生的id必须不同。

<!-- more -->

Snowflask 算法在工作中经常会用，平常做开发涉及到需要生成自增 id，也会第一个想到这个算法，具体的算法详解 [Twitter-Snowflake，64位自增ID算法详解 ](http://www.lanindex.com/twitter-snowflake%EF%BC%8C64%E4%BD%8D%E8%87%AA%E5%A2%9Eid%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3/) 这篇文章做了详细介绍，我不在多做口舌，只是着重总结几种语言的实现方式，以便以后自己查阅。

## Python
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import sys
import time
import random
import threading


class Snowflake(object):
    region_id_bits = 2
    worker_id_bits = 10
    sequence_bits = 11

    MAX_REGION_ID = -1 ^ (-1 << region_id_bits)
    MAX_WORKER_ID = -1 ^ (-1 << worker_id_bits)
    SEQUENCE_MASK = -1 ^ (-1 << sequence_bits)

    WORKER_ID_SHIFT = sequence_bits
    REGION_ID_SHIFT = sequence_bits + worker_id_bits
    TIMESTAMP_LEFT_SHIFT = (sequence_bits + worker_id_bits + region_id_bits)

    def __init__(self, worker_id, region_id=0):
        self.twepoch = 1495977602000
        self.last_timestamp = -1
        self.sequence = 0

        # assert 0 <= worker_id <= Snowflake.MAX_WORKER_ID
        # assert 0 <= region_id <= Snowflake.MAX_REGION_ID

        self.worker_id = worker_id
        self.region_id = region_id

        self.lock = threading.Lock()

    def generate(self, bus_id=None):
        return self.next_id(
            True if bus_id is not None else False,
            bus_id if bus_id is not None else 0
        )

    def next_id(self, is_padding, bus_id):
        with self.lock:
            timestamp = self.get_time()
            padding_num = self.region_id

            if is_padding:
                padding_num = bus_id

            if timestamp < self.last_timestamp:
                try:
                    raise ValueError(
                        'Clock moved backwards. Refusing to'
                        'generate id for {0} milliseconds.'.format(
                            self.last_timestamp - timestamp
                        )
                    )
                except ValueError:
                    print(sys.exc_info[2])

            if timestamp == self.last_timestamp:
                self.sequence = (
                                    self.sequence + 1) & Snowflake.SEQUENCE_MASK
                if self.sequence == 0:
                    timestamp = self.tail_next_millis(self.last_timestamp)
            else:
                self.sequence = random.randint(0, 9)

            self.last_timestamp = timestamp

            res_id = (
                (
                    timestamp - self.twepoch) << Snowflake.TIMESTAMP_LEFT_SHIFT |
                (padding_num << Snowflake.REGION_ID_SHIFT) |
                (self.worker_id << Snowflake.WORKER_ID_SHIFT) |
                self.sequence
            )

            return res_id

    def tail_next_millis(self, last_timestamp):
        timestamp = self.get_time()
        while timestamp <= last_timestamp:
            timestamp = self.get_time()
        return timestamp

    def get_time(self):
        return int(time.time() * 1000)



if __name__ == '__main__':
    print(Snowflake(0).generate())
```
## Java
```java
package common;

/**
 * timestamp + bizId + workId + sequence
 * */
public class UKeyWorker{

    private final static long twepoch = 1404878190828L;

    //机器标识位数（每种业务支持多少worker-thread）
    private final static long workerIdBits = 5L;
    //业务标识位数（预留）
    private final static long bizIdBits = 6L;

    //机器标识最大值
    private final static long maxWorkerId = -1L ^ -1L << UKeyWorker.workerIdBits;
    //业务标识最大值
    private final static long maxBizId = -1L ^ -1L << UKeyWorker.bizIdBits;

    //毫秒内自增位数
    private final static long sequenceBits = 12L;

    // 机器标识偏左移
    private final static long workerIdShift = UKeyWorker.sequenceBits;
    // 业务标识偏左移
    private final static long bizIdShift = UKeyWorker.sequenceBits
            + UKeyWorker.workerIdBits;
    // 时间毫秒偏左移
    private final static long timestampShift = UKeyWorker.sequenceBits
            + UKeyWorker.workerIdBits + UKeyWorker.bizIdBits;

    //序列号Mask
    private final static long sequenceMask = -1L ^ -1L << UKeyWorker.sequenceBits;
    //机器标识Mask
    private final static long workerIdMask = UKeyWorker.maxWorkerId << UKeyWorker.workerIdShift;
    //业务标识Mask
    private final static long bizIdMask = UKeyWorker.maxBizId << UKeyWorker.bizIdShift;
    //时间戳Mask
    private final static long timestampMask = Long.MAX_VALUE
            ^ (UKeyWorker.sequenceMask | UKeyWorker.workerIdMask | UKeyWorker.bizIdMask);

    //最后的时间戳
    private long lastTimestamp = -1L;

    private final long workerId;
    private final long bizId;

    private long sequence = 0L;

    public UKeyWorker(final long workerId, final long bizId) {
        super();
        if (workerId > UKeyWorker.maxWorkerId || workerId < 0) {
            throw new IllegalArgumentException(String.format(
                    "worker Id can't be greater than %d or less than 0",
                    UKeyWorker.maxWorkerId));
        }
        this.workerId = workerId;

        if (bizId > UKeyWorker.maxBizId || workerId < 0) {
            throw new IllegalArgumentException(String.format(
                    "biz Id can't be greater than %d or less than 0",
                    UKeyWorker.maxBizId));
        }
        this.bizId = bizId;

    }

    public long getId() {
        long id = nextId();
        return id;
    }

    public synchronized long nextId() {
        long timestamp = this.timeGen();

        // 时间发生错误
        if (timestamp < this.lastTimestamp) {
            throw new RuntimeException(
                    String
                            .format(
                                    "Clock moved backwards.  Refusing to generate id for %d milliseconds",
                                    this.lastTimestamp - timestamp));
        }

        //毫秒内
        if (this.lastTimestamp == timestamp) {
            this.sequence = (this.sequence + 1) & UKeyWorker.sequenceMask;
            if (this.sequence == 0) {
                timestamp = this.tilNextMillis(this.lastTimestamp);
            }
        } else {
            this.sequence = 0;
        }

        this.lastTimestamp = timestamp;

        //计算
        long nextId = ((timestamp - UKeyWorker.twepoch << UKeyWorker.timestampShift)) |
            (this.bizId << UKeyWorker.bizIdShift) |
            (this.workerId << UKeyWorker.workerIdShift) |
            (this.sequence);

        return nextId;
    }

    private long tilNextMillis(final long lastTimestamp) {
        long timestamp = this.timeGen();
        while (timestamp <= lastTimestamp) {
            timestamp = this.timeGen();
        }
        return timestamp;
    }

    private long timeGen() {
        return System.currentTimeMillis();
    }

    public static long getSequence(final long id){
        return (id & UKeyWorker.sequenceMask);
    }

    public static long getWorkerId(final long id){
        return (id & UKeyWorker.workerIdMask) >> UKeyWorker.workerIdShift;
    }

    public static long getBizId(final long id){
        return (id & UKeyWorker.bizIdMask) >> UKeyWorker.bizIdShift ;
    }

    public static long getTimestamp(final long id) {
        return (id & UKeyWorker.timestampMask) >> UKeyWorker.timestampShift;
    }

    public static void main(String[] args) {
        UKeyWorker sf = new UKeyWorker(31L, 63L);
        System.out.println(sf.getId());
    }

}
```
