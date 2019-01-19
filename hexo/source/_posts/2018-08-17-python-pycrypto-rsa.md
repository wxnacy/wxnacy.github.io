---
title: Python 使用 pycrypto 进行 rsa 公私钥加解密和签名验证
date: 2018-08-17 16:43:08
tags: [python]
---

公私钥加密是现在公认最安全的加密方式。因为普通的对称加密方式，加密和解密是用相同的秘钥来进行的，那不管这个算法多么复杂，只要你需要将秘钥发送给解密方，这个秘钥就一定可能会泄露给第三方，为此我们只能定期更改秘钥来减少加密信息被破解的几率，但这明显不是一个很好的方法。

<!-- more --><!-- toc -->
如果你的数据需要绝对的保密，那已经要选用公私钥加密的方式，简单来说公私钥的原理为：

- 公钥加密，私钥解密
- 私钥签名，公钥验证


## 生成秘钥

在 Unix 系统中可以很方便的生成公私钥

```bash
$ ssh-keygen -t rsa -C "your_email"
```

使用你自己的邮箱，一路回车即可生成 `id_rsa, id_rsa.pub` 秘钥对，在目录 `~/.ssh` 中，你也可以根据提示生成自己想要的名字

## 加解密

很多人开始接触非对称加密时，经常分不清公私钥到底谁来加密谁来解密，其实只要搞清楚公私钥由谁来保管就行了。

公钥，顾名思义是可以公之于众的秘钥，理论上谁都可以拿到。如果公钥可以解密的话，那岂不是跟用明文没什么区别了吗？

而私钥，只有我自己可以拥有，那密文也就只有我自己能破解。

假设我老婆要对我说，我爱你，但是她不想让别人听见，所以使用了我给她的公钥对其进行加密，私钥只在我这里，所以即使任何人拿到公钥和密文都不能听到这句话。

在 Python 中使用 `pycrypto` 模块可以进行公私钥的加解密算法。

**下载**

```bash
$ pip install pycrypto
```

**代码**

py 版本 3.5+

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

def encrypt(message, pub_rsa_path):
    '''使用公钥加密'''
    with open(pub_rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(message.encode()))
        return cipher_text

def decrypt(secret_message, rsa_path):
    '''使用私钥解密'''
    with open(rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(secret_message), random_generator)
        return text


if __name__ == "__main__":
    plain = 'message'
    pub_rsa_path = '/Users/wxnacy/.ssh/id_rsa.pub'
    rsa_path = '/Users/wxnacy/.ssh/id_rsa'

    print('明文：', plain)
    secret = encrypt(plain, pub_rsa_path)
    print('加密文：', secret)
    text = decrypt(secret, rsa_path)
    print('解密文：', text)

```

## 签名验证

刚才说了，随便有个公钥的人对信息加密，我就能进行解密，那公钥是公开的，我怎么知道解密的明文是我老婆要对我说的话呢，万一是谁朝我借钱怎么办。

这时候我老婆需要对“我爱你”进行签名，我解密出明文后，要对签名进行验证，验证通过后，我就知道这确实是我老婆说的话了。

签名的公私钥顺序跟加密是反过来的，我老婆在自己的机器上也生成一对秘钥，然后将公钥给我，私钥保留，然后她用私钥签名，我用公钥验证，这时候虽然任何人拿到公钥都可以验证，但是不能拿到明文，只是验证明文没有被篡改。

这样我们双方互换公钥，各自保留私钥，加密和签名双管齐下，互发消息都可以做到非常安全。


**代码**

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

def signature(message, rsa_path):
    '''使用私钥签名'''
    with open(rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode())
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)

        return signature

def verify_signature(message, signature, pub_rsa_path):
    '''验证签名'''
    with open(pub_rsa_path) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # Assumes the data is base64 encoded to begin with
        digest.update(message.encode())
        print(digest)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        return is_verify


if __name__ == "__main__":
    plain = 'message'

    sign_pub_rsa_path = '/Users/wxnacy/.ssh/test_gmail_rsa.pub'
    sign_rsa_path = '/Users/wxnacy/.ssh/test_gmail_rsa'

    sign = signature(plain, sign_rsa_path)
    print('签名：', sign)
    flag = verify_signature(plain, sign, sign_pub_rsa_path)
    print('验证结果：', flag)
```

[demo](https://github.com/wxnacy/study/blob/master/python/simple/rsa_encrypt.py)
