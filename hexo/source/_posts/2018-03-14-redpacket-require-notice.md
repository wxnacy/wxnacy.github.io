---
title: 设计一个领取红包的活动需要注意的点
tags:
  - 开发
date: 2018-03-14 14:49:40
---


前段时间开发了一个领取红包的功能，有很多需要注意的点，是下次需要注意的
<!-- more -->

- 检查用户是否有资格领取红包的定时任务需要有时间期限
- 活动到期后，领取接口需要做判断
- 需要考虑用户保存领取红包的二维码或网页信息的情况，设计每日任务时效机制

## 红包分配思路
### 实例一
给定一个固定的活动日期，固定的奖金总额，有一个可以预见的参与人数，有一个每天领取可以接受的上下限金额，如何分配用户领取的随机金额

有一种方式是可以预先生成足够多的红包金额数组，每个参与的用户根据领取的索引在获取该得到的红包金额，算法如下
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import random

def get_redpacket_amounts():
    """
    活动时间：39天
    活动金额：$2300
    参与人数：288
    平均每天领取金额：2300 / 39  =  $59
    每天平均领取金额：59 / 288  = $0.2
    期望最低领取：$0.1
    期望最高领取：$8
    算法：首先生成一个长度为每天最大参与人数的数组，每个元素的值为活动可以期望的最小金额，然后遍历数组，给定几个位置赋值为可以接受的最大金额，剩下的位置根据当天奖金池随机分配，直到全部分完
    """
    daily_total = 5900
    min_amount = 10
    total = 288
    normal_range = 91

    big_amount = daily_total - (min_amount * total)

    res = [min_amount] * total
    for i in range(len(res)):
        n = res[i]
        if i == 0 or i == 9:
            rand =  int(random.uniform(600, 791))
        else:
            ran = normal_range if big_amount >=normal_range else big_amount
            rand =  int(random.uniform(0, ran)
                    ) if ran > 0 else 0
        big_amount = big_amount - rand
        res[i] = n + rand

    return res

if __name__ == "__main__":
    print(get_redpacket_amounts())
```

