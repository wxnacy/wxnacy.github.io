---
title: Python 使用 PyCrypto 进行散列和加解密算法
tags:
  - python
date: 2018-03-10 16:51:46
---


我在 [Node 使用 crypto-js 进行散列和加解密算法](/2017/12/20/cryptojs/)中简单介绍了什么是散列和加解密算法，并了解了在 Node 中的使用方式，今天主要介绍如何在 Python 进行这些操作。

<!-- more --><!-- toc -->
[PyCrypto](https://www.dlitz.net/software/pycrypto/) 提供 安全的哈希函数和各种加密算法，支持Python 2.1 以上
## 下载
```bash
$ pip install pycrypto
```
## MD5
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from Crypto.Hash import MD5

def md5(text):
    hash = MD5.new()
    hash.update('message'.encode('utf-8'))
    return hash.hexdigest()
if __name__ == '__main__':
    print(md5('message'))   # => '78e731027d8fd50ed642340b7c9a63b3'
```
其他哈希函数见[文档](https://www.dlitz.net/software/pycrypto/api/current/)
另外还有一种方法不需要外部依赖，使用 Python 的 hashlib 模块
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import hashlib

def md5(text):
    hash = hashlib.md5()
    hash.update(text.encode('utf-8'))
    return hash.hexdigest()

if __name__ == "__main__":
    print(md5('message'))
```

## AES
[这里](https://www.dlitz.net/software/pycrypto/api/current/)是 AES 的文档，只看他的文档运行加密过程是没问题，但是想要在项目里应用就比较蛋疼，首先加密的是个二进制数据就是个问题，所以我写了一个 Demo 来描述在项目中加解密的过程。
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from Crypto import Random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class AESUtils():
    @classmethod
    def generate_key(cls):
        """
        在对称密码中使用的密钥。 它必须是16（AES-128），24（AES-192）或32（AES-256）字节长。
        先用 Random 生成一个16位的二进制数据，并转为16进制数据变成 32 位
        """
        return b2a_hex(Random.new().read(16)).decode('utf-8')

    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
        self.iv = Random.new().read(16)

    def encrypt(self, text):
        """
        需要加密的文本，长度必须为 16 的倍数，不够的位用空格补全
        """
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        aes = AES.new(self.key, self.mode, self.iv)
        secret = aes.encrypt(text)
        # 加密后返回的是二进制数据，需要转为 16 进制的字符串
        secret = b2a_hex(secret).decode('utf-8')
        return secret

    def decrypt(self, secret):
        """
        解密时先将文本转为二进制在操作
        """
        aes = AES.new(self.key, self.mode, self.iv)
        plain_text = aes.decrypt(a2b_hex(secret)).decode("utf-8")

        return plain_text.rstrip('\x00')

if __name__ == "__main__":
    key = AESUtils.generate_key()
    print(key)
    aes = AESUtils(key)
    secret = aes.encrypt('message')
    print(secret)
    plain = aes.decrypt(secret)
    print(plain)
```
其他的对称加密类型详见[文档](https://www.dlitz.net/software/pycrypto/api/current/)

- 相关阅读
- [MD5，SHA，HMAC ，AES 在线加密计算](/2017/12/19/tool-crypto/)
- [Node 使用 crypto-js 进行散列和加解密算法](/2017/12/20/cryptojs/)
