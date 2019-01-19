---
title: Node 如何发送邮件
date: 2017-12-16 22:30:07
tags: [node]
---

在 Node 中发送邮件是很简单的，[Nodemailer](https://nodemailer.com/about/) 包提供了很完善的接口来实现该功能。

<!-- more --><!-- toc -->
## 下载
npm
```bash
$ npm install --save nodemailer
```
yarn
```bash
$ yarn add nodemailer
```
## 使用
使用起来很简单先看下官方的例子
```javascript
'use strict';
const nodemailer = require('nodemailer');

nodemailer.createTestAccount((err, account) => {
    let transporter = nodemailer.createTransport({
        host: 'smtp.mxhichina.com', // smtp 地址，我使用的阿里企业邮箱
        port: 25,                   // smtp 端口
        secure: false,              // 如果不是 465 的端口，就是用 false
        auth: {
            user: 'your_name',      // 邮箱名
            pass: 'your_password'   // 邮箱密码
        }
    });

    // setup email data with unicode symbols
    let mailOptions = {
        from: 'info@wxnacy.com',    // 发送人邮箱
        to: 'wxnacy@gmail.com',     // 接收人邮箱，多个使用数组或用逗号隔开
        subject: 'Hello ✔',         // 主题
        text: 'Hello world?',       // 邮件正文
    };

    // send mail with defined transport object
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return console.log(error);
        }
        console.log('Message sent: %s', info.messageId);
    });
});
```
如果你有过类似邮件服务的开发经验，看到上面这些参数大概就能改成自己的进行工作了
，再简单使用的基础上，该模块还提供了很多高级功能。

## 高级功能
抄送/密送，跟 `to` 参数规则一样
```java
let mailOptions = {
    ...
    cc: ['aaa@aa.com', 'bbb@bb.com'],   // 抄送
    bcc: 'xxx@xx.com, bbb@bb.com'       // 密送
}
```
发送 html 文本
```java
let mailOptions = {
    ...
    html: "<div>Hello World</div>"
}
```
使用 `attachments` 参数发送附件，`first.txt` 为直接以文本作为附件，`json.js` 以
本地文档作为附件
```javascript
let message = {
    attachments: [
        {
            filename: 'first.txt',
            content: 'hello world!'
        },
        {
            filename: 'json.js',
            path: './json.js'
        }
    ]
}
```
基于 `html` 和 `attachements` 两个参数可以达到在文本中显示图片的功能，在以图片
地址为附件的基础上，增加一个 `cid` ，并在 html 文本中使用如下引用，既可显示图片
```javascript
let message = {
    ...
    html: 'Embedded image: <img src="cid:unique@nodemailer.com"/>',
    attachments: [{
        filename: 'image.png',
        path: '/path/to/file',
        cid: 'unique@nodemailer.com' //same cid
    }]
}
```

如果还想了解更多功能，请看[文档](https://nodemailer.com/message/)

