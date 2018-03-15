#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import hashlib

def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    a = 1
    print((a << 53) -1)
    print(1 << 48)
    s = 1 << 5
    w = 1
    i = 1
    print((s << 48 ) + (w << 43 ) + i)
    print(1 << 42)
    print(1 << 63)
    for i in range(10):
        print(i, md5(str(i)))
