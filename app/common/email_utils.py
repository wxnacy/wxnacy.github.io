#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''邮件'''
__author__ = "wenxiaoning(wenxiaoning@gochinatv.com)"
__copyright__ = "Copyright of GoChinaTV (2017)."

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
# mail_host = "smtp.mxhichina.com"  # 设置服务器
# mail_user = "account@wxnacy.com"  # 用户名
# mail_pass = "Wxnacy140111"  # 口令
#
# sender = 'account@wxnacy.com'
# receivers = ['371032668@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
# except smtplib.SMTPException as e:
#     print(e)


class Email():
    def __init__(self, host='smtp.mxhichina.com', user='account@wxnacy.com',
                 password='Wxnacy140111', sender='account@wxnacy.com',
                 sender_name='温总博客'):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(user, password)

            self.client = smtpObj
            self.sender = sender
            self.sender_name = sender_name
        except smtplib.SMTPException as e:
            print(e)

    def send(self, receivers, subject, message):
        message = MIMEText(message, 'plain', 'utf-8')
        message['From'] = Header(self.sender_name, 'utf-8')
        # message['To'] = Header('wen', 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        self.client.sendmail(self.sender, receivers, message.as_string())
        pass


if __name__ == '__main__':
    e = Email()
    e.send(['371032668@qq.com','18311233541@163.com'],'邀请您','<div>欢迎您</div>')
