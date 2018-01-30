---
title: 身份证号码校验规则
date: 2017-08-05
tags: [算法]
---

[原文:http://www.icloudyin.com/?p=66](http://www.icloudyin.com/?p=66)

18位身份证号码组成：`ddddddyyyymmddxxsp`共18位，其中：其他部分都和15位的相同。年份代码由原来的2位升级到4位。最后一位为校验位。

## 校验规则：
- 十七位数字本体码加权求和公式
```bash
S = Sum(Ai * Wi), i = 0, … , 16 ，先对前17位数字的权求和
Ai:表示第i位置上的身份证号码数字值
Wi:表示第i位置上的加权因子
Wi: 7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2
```
- 计算模
```bash
Y = mod(S, 11)
```

- 通过模得到对应的校验码
```bash
Y: 0 1 2 3 4 5 6 7 8 9 10
校验码: 1 0 X 9 8 7 6 5 4 3 2
```

## java

```java
static String getCheckCode(String idCard){
    static String[] Wi = { "7", "9", "10", "5", "8", "4", "2", "1", "6", "3", "7",
        "9", "10", "5", "8", "4", "2" };
    int sum = 0;
    for( int i = 0 ; i < 17 ; i ++)
    {
        sum = sum + Integer.parseInt(String.valueOf(idCard.charAt(i))) * Integer.parseInt(String.valueOf(Wi[i]));
    }
    int T  = sum % 11;
    int R = (12 -T) % 11;
    if( R == 10 )
        return "X";
    else {
        return String.valueOf(R);
    }
}
```


## python

```python
def check_identity_card(card):
    wi = ["7", "9", "10", "5", "8", "4", "2", "1", "6", "3", "7", "9", "10","5", "8", "4", "2"]
    total = 0
    card = list(card)
    index = 0
    for item in card:
        total += ord(item) * int(wi[index])
        index += 1
        t = total % 11
    r = (12 - t) % 11
    if r == 10:
        return "X"
    else:
        return r
```
