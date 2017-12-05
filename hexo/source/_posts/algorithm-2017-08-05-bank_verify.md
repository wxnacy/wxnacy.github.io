---
title: 银行卡校验规则(Luhn算法)
date: 2017-08-05
tags: [算法]
---

[原文:http://www.icloudyin.com/?p=61](http://www.icloudyin.com/?p=61)

- 检验数字算法（Luhn Check Digit Algorithm），也叫做模数10公式，是一种简单的算法，用于验证银行卡、信用卡号码的有效性的算法。对所有大型信用卡公司发行的信用卡都起作用，这些公司包括美国Express、护照、万事达卡、Discover和用餐者俱乐部等。这种算法最初是在20世纪60年代由一组数学家制定，现在Luhn检验数字算法属于大众，任何人都可以使用它。
- 将卡号上的每个数字乘上其权重（weight），如果卡号上的数字个数是偶数，那么第一个数字的权重就是2，若是奇数，那么权重就给1，剩下来的数字，根据第一个数字依序给定。例如某信用卡卡号的数字个数为偶数，那么从第一个数字开始的权重依序为 2、1、2、1、2、1 …。
- 如果数字乘上自己的权重后比9还大，那么就从这加权数字里扣除9。
- 接下来将所有处理过的加权数字全部加总起来，并且除以10，取其余数。

## java
```java
int sum = 0;
	boolean even = true;
	for ( int index = digits.size() - 1; index >= 0; index-- ) {
		int digit = digits.get( index );

		if ( even ) {
			digit <<= 1;
		}
		if ( digit > 9 ) {
			digit -= 9;
		}
		sum += digit;
		even = !even;
	}
	return ( 10 - ( sum % 10 ) ) % 10;

```
## python
```python
def check_bank_card(card_num):
    """检查银行卡的合法性"""
    total = 0
    even = True
    if isinstance(card_num, int):
        card_num = str(card_num)
    check_num = card_num[-1]
    for item in card_num[-2::-1]:
        item = int(item)
        if even:
            item <<= 1
        if item > 9:
            item -= 9
        total += item
        even = not even
    return int(check_num) is (10 - (total % 10)) % 10

```

