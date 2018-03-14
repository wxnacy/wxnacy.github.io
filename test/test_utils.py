#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

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
