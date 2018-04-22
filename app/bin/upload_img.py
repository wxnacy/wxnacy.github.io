#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from app.common.aliyun import OSSClient
from app.common.image import Image
from app.config import BaseConfig

import sys
import time
import requests
from datetime import date

oss = OSSClient()

def get_filename(uri):
    fp = uri.rsplit('/', 1)
    filename = uri
    if len(fp) == 1:
        filename = fp[0]
    else:
        filename = fp[1]
    return filename

def upload_img(uri):
    """上传图片"""
    fn = get_filename(uri)
    key = f'upload/{time.time()}-{fn}'
    bk = BaseConfig.ALIYUN_BUCKET_IMG
    if 'http' in uri:
        res = requests.get(uri)
        f = res.content
    else:
        f = open(uri, 'rb')

    return oss.put_object(bk, key, f)


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print('Uage: python upload_img.py file_path')
    else:

        filepath = args[1]
        url = upload_img(filepath)
        print(url)
