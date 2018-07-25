#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import requests
import unittest
import xmltodict
import json

#  url = 'http://localhost:8010/tmdapi/v1/wx'
URL = 'http://localhost:8002/api/v1/wx/mp_callback'
#  URL = 'http://localhost:8010/tmdapi/v1/wx/third/app/mp_callback'

class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def teardown(self):
        pass

    def test_check_request(self):
        url = '{}?signature=ed90274ee0fa0bfd76909986a89cc2e43234ad70&timestamp=1531967300&nonce=1593529105&echostr=test_str'.format(URL)
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content, b'test_str')

    def test_get_body(self):
        url = '{}?signature=8dbf245f43e4096538de19cae1bd7749bba71ac0&timestamp=1531983596&nonce=955439717&echostr=ss&msg_signature=1a49bd8999f2e9e75a98adf55599453daa4c7891'.format(URL)

        data = '<xml> <ToUserName><![CDATA[gh_96c685096fbd]]></ToUserName> <Encrypt><![CDATA[awoq2zcSPV4GAjg5u8Jr5E2G4/dUS3FbbTgeDlhYOHKxC2a7Bb+WROg6gEUUlZdgokjgUHHdPikMI/GvqGKoQ66HLxIFf54xq8FdFdXLLoZBlqHztUL3wV/T1uv25IkmlVe7zfkOG9erKemIw74gKuNzimm49Vam/OJVoYnKPYMhkWJcz9YQcP2y79ZMA6giEnGTVnAPFIc0wgpPMbpOgfih8s7H/NhE+uA+b9zdbdR5eynW3qbFtXqjRz2hxOb/LGo7djibx6OX5E6PaZ7anKxiq9psPNCo0h43h/7Gy/zT+E0BwgQg9EdjEmD/Dets8pSK7JX5WLO/oAToYVYDDtsIvFRlXK1rbn1rd9eIAj2IgrsrDFM3BGjHHybKTGOf3luSADlnxtXS4rjo8/oaZeyOe4O0JxTLvwwhlew5wd0=]]> </Encrypt> </xml>'

        print(xmltodict.parse(data))
        print(json.loads(json.dumps(xmltodict.parse(data))))
        res = requests.post(url, data=data)

        self.assertEqual(res.status_code, 200)
        res_data = json.loads(json.dumps(xmltodict.parse(res.text)))
        self.assertEqual(res_data['xml']['Content'], '啊')
        #  res_data = json.


if __name__ == '__main__':
    unittest.main()
