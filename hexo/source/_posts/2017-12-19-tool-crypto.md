---
title: MD5，SHA，HMAC ，AES 在线加密计算
date: 2017-12-19 15:03:03
tags: [算法]
---

签名和加解密平常偶尔会用到，又不想每次都去 google 找，干脆自己写了一个在线工具。
<!-- more -->
文本： <textarea id="msg" style="width: 50%">message</textarea>
<br/>
KEY: <input id="key" value="message_key" style="width: 30%"/>
<button id="encrypt" onClick="create_crypto('default')">签名</button> <button id="encryptHmac" onClick="create_crypto('hmac')">HMAC 签名</button> <button id="encryptAES" onClick="create_crypto('aes_encrypt')">AES 加密</button> <button id="decryptAES" onClick="create_crypto('aes_decrypt')">AES 解密</button> <button id="encryptDES" onClick="create_crypto('des_encrypt')">DES 加密</button> <button id="decryptDES" onClick="create_crypto('des_decrypt')">DES 解密</button> <button id="encryptTDES" onClick="create_crypto('tdes_encrypt')">TripleDES 加密</button> <button id="decryptTDES" onClick="create_crypto('tdes_decrypt')">TripleDES 解密</button> <button id="encryptRabbit" onClick="create_crypto('rabbit_encrypt')">Rabbit 加密</button> <button id="decryptRabbit" onClick="create_crypto('rabbit_decrypt')">Rabbit 解密</button>




<div id="hash" style="display: none">
MD5
<span id="md5" ></span>
SHA1
<span id="sha1" ></span>
SHA256
<span id="sha256" ></span>
SHA512
<span id="sha512" ></span>
</div>

<div id="crypto" style="display: none">
结果
<span id="result" ></span>
</div>

- **签名** 现在支持的签名为 MD5，SHA1，SHA256，SHA512，以及 Hmac 加密签名
- **加密／解密** 现在支持 AES 算法的加解密

## 参考
- [https://1024tools.com/hmac](https://1024tools.com/hmac)
- [http://www.yuangongju.com/encrypt](http://www.yuangongju.com/encrypt)
