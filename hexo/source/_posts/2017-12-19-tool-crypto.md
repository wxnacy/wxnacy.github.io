---
title: MD5，SHA，HMAC 在线加密计算
date: 2017-12-19 15:03:03
tags: [算法]
---

文本： <textarea id="msg" style="width: 50%">message</textarea>
<br/>
KEY: <input id="key" value="message_key" style="width: 30%"/>
<button id="encrypt" onClick="create_crypto('default')">签名</button> <button id="encryptHmac" onClick="create_crypto('hmac')">HMAC 签名</button> <button id="encryptAES" onClick="create_crypto('aes_encrypt')">AES 加密</button> <button id="decryptAES" onClick="create_crypto('aes_decrypt')">AES 解密</button>

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
