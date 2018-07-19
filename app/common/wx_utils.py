#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''加密工具'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import logger
from app.common.security import AESecurity
import base64
import hashlib


EAKEY = 'F3uIXPvYZ8nmpPVhazFkertj25fry8OcINM87xRe4kg'
token = 'F3uIXPvYZ8nmpPVhazFkert'


#  mmutableMultiDict([('signature', 'ed90274ee0fa0bfd76909986a89cc2e43234ad70'), ('echostr', '2080843817504733135'), ('timestamp', '1531967300'), ('nonce', '1593529105')])

ts ='1531967300' 
nonce = '1593529105'
signature = 'ed90274ee0fa0bfd76909986a89cc2e43234ad70'


class WXSecurity():

    def __init__(self, token, encoding_aes_key):
         self.token = token
         self.encoding_aes_key = encoding_aes_key

    def check_get_request(self, signature, timestamp, nonce):
        data = [self.token, str(timestamp), str(nonce)]
        data.sort()
        sha1 = hashlib.sha1()
        sha1.update(''.join(data).encode("utf-8"))
        sign = sha1.hexdigest()
        logger.debug(sign)
        return sign == signature



if __name__ == "__main__":
    print(f'{EAKEY}=')
    key = base64.b64decode(f'{EAKEY}=')
    print(key)
    print(len(key))
    aes = AESecurity(key)
    s = aes.encrypt('test')
    print(s)
    t = aes.decrypt(s)
    print(t)
    print([token, ts, nonce].sort())

    wxs = WXSecurity(token, EAKEY)
    #  flag = wxs.check_get(signature, ts, nonce)
    #  print(flag)
