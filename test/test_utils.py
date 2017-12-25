#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:


from app.common import utils
import os
import sys
import time
from datetime import datetime
import msgpack

class User():
    def __init__(self):
        self.name = 'wxnacy'

    def __str__(self):
        return self.name

if __name__ == "__main__":

    #  print(time.time())
    #  utc = time.gmtime(time.time())
    #  print(utc)
    #  res = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
    #  print(res)
    #  t = '2017-12-10 16:37:17'
    #  t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    #  res = int(time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S')))
    #  print(res)
    #  print(datetime.now().timestamp())
    #  res = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    #  print(res)
    #  u = User()
    #  print(u)
    #  res = msgpack.packb(u, use_bin_type=True)
    #  print(res)
    #  res = msgpack.unpackb(res, encoding='utf-8')
    #  print(res)
    useful_dict = {
        "id": 1,
        "created": datetime.now(),
    }

    def decode_datetime(obj):
        if '__datetime__' in obj:
            #  print(obj)
            obj = datetime.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S.%f")
        return obj

    def encode_datetime(obj):
        if isinstance(obj, datetime):
            return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S.%f")}
        return obj


    packed_dict = msgpack.packb(useful_dict, default=encode_datetime)
    print(packed_dict)
    this_dict_again = msgpack.unpackb(packed_dict, object_hook=decode_datetime,
            encoding='utf-8')
    print(this_dict_again)
