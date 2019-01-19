---
title: Python 计算 url 短连接
date: 2018-06-21 20:17:14
tags: [python]
---

Python 计算 url 短连接

<!-- more --><!-- toc -->
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import hashlib

def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

code_map = (
        'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' ,
        'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' ,
        'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' ,
        'y' , 'z' , '0' , '1' , '2' , '3' , '4' , '5' ,
        '6' , '7' , '8' , '9' , 'A' , 'B' , 'C' , 'D' ,
        'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' ,
        'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' ,
        'U' , 'V' , 'W' , 'X' , 'Y' , 'Z'
        )

def generate_short(long_url):
    '''生成短连接'''
    hkeys = []
    hex_text = md5(long_url)
    for i in range(0, 4):
        n = int(hex_text[i*8:(i+1)*8], 16)
        v = []
        e = 0
        for j in range(0, 5):
            x = 0x0000003D & n
            e |= ((0x00000002 & n ) >> 1) << j
            v.insert(0, code_map[x])
            n = n >> 6
        e |= n << 5
        v.insert(0, code_map[e & 0x0000003D])
        hkeys.append(''.join(v))

    return hkeys[0]

if __name__ == '__main__':
    print(generate_short('https://wxnacy.com'))
```
