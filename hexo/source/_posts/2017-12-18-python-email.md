---
title: Python SMTP发送邮件
date: 2017-12-18 21:02:36
tags: [python]
---

> SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

<!-- more --><!-- toc -->
Python 中的 smtplib 模块，对 smtp 进行了简单的封装，提供了一套发送邮件的 api

## 构造 SMTP
```python
import smtplib
smtp = smtplib.SMTP()
smtp.connect(host, port)
smtp.login(user, password)
```
- host SMTP 服务器主机，ip 或域名
- port SMTP 端口号，一般为 25
- user 发送人邮箱名
- password 发送人密码

## 消息体
```python
from email.mime.text import MIMEText
from email.header import Header

message = MIMEText(msg, mime_type, 'utf-8')
message['From'] = Header('发件人', 'utf-8')
message['To'] = Header('收件人', 'utf-8')
message['Subject'] = Header('主题', 'utf-8')
```
- msg 邮件正文，普通文本或 html 代码
- mime_type 消息类型，html 或 text
`From` 和 `To` 不是必填字段，但是不填的话，发送人和接受人的位置就会显示空。

## 发送
```python
smtp.sendmail(sender, receivers, msg)
```
- sender 发送人邮件
- receivers 接受人邮件，数组
- msg 消息体

## Hello World
完成的邮件发送代码如下
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp = smtplib.SMTP()
smtp.connect(host, port)
smtp.login(user, password)

message = MIMEText('Hello World', 'text', 'utf-8')
message['From'] = Header('wxnacy', 'utf-8')
message['To'] = Header('朋友', 'utf-8')
message['Subject'] = Header('Hello World', 'utf-8')

smtp.sendmail('wxnacy@gmail.com', ['bbb@bb.com'], message.as_string())
```

## 抄送／密送
在 smtplib 中发送邮件没有普通和抄送之分，都是放在 `receivers` 中，只是在头信息中区分开
```python
cc = ['bb@bbb.com', 'cc@ccc.com']
message['Cc'] = Header(','.join(cc), 'utf-8')   # 抄送
message['Bcc'] = Header(','.join(cc), 'utf-8')  # 密送
```

## 附件
发送附件的时候需要引入新模块 `MIMEMultipart`
```python
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart()
message['From'] = Header("发送人", 'utf-8')
message['To'] =  Header("接受人", 'utf-8')
message['Subject'] = Header('附件测试', 'utf-8')

message.attach(MIMEText('这是一段正文', 'plain', 'utf-8'))

att1 = MIMEText(open('./test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

smtp.sendmail('wxnacy@gmail.com', ['bb@bbb.com'], message.as_string())
```

## HTML 文本中显示图片
使用 `MIMEImage` 模块可以接收图片格式数据，配合 `MIMEMultipart` 以附件的形式发送，并显示在文本中
```python
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("菜鸟教程", 'utf-8')
msgRoot['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)


mail_msg = """
           <p>Hello World</p>
           <p><img src="cid:image1"></img></p>
           """
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('./test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
self.client.sendmail(self.sender, receivers, msgRoot.as_string())
```
图片以附件发送，并指定 `cid` ，在文本中引用该 id 即可

## 参考
- [email](https://docs.python.org/3.4/library/email-examples.html)
- [Python3 SMTP发送邮件](http://www.runoob.com/python3/python3-smtp.html)
