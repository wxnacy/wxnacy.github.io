#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from PIL import Image as I
import io
import requests


class Image():
    def __init__(self, *args, **kwargs):
        self.path = args[0]
        if self.path.startswith('http'):
            self.is_network = True
            res = requests.get(self.path)
            self.data = res.content
            self.image = I.open(io.BytesIO(self.data))
        else:
            self.is_local = True
            self.image = I.open(self.path)

        self.format = self.image.format.lower()
        if self.format == 'jpeg':
            self.format = 'jpg'


if __name__ == '__main__':
    # source env.sh && python api/common/image.py
    url = 'http://www.bing.com/cr?IG=2AFFA7974D70440BACAD567B6530C929&CID=38A99FD1864D605015F79536878D6142&rd=1&h=erqob2mKPmQGaBK4bLE99WJuiRE6RMBm44n96T55bxs&v=1&r=http%3a%2f%2fws2.cdn.caijing.com.cn%2f2014-03-23%2f114032711.jpg&p=DevEx,5014.1'

    i = Image(url)
    print(i.format)
