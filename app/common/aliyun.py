#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' aliyun 的工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import app


import oss2
import requests
from datetime import date
from datetime import datetime

ENDPOINT = 'oss-cn-beijing.aliyuncs.com'
BUCKET_IMG = 'wxnacy-img'


class OSSClient():
    def __init__(self, access_key=app.config['ALIYUN_ACCESS_KEY'],
                 secret_key=app.config['ALIYUN_SECRET_KEY'],
                 endpoint=ENDPOINT):
        self.endpoint = endpoint
        self.auth = oss2.Auth(access_key, secret_key)

    def put_object(self, bucket_name, key, data, headers=None,
                   progress_callback=None):
        """
        上传文本到aliyun
        :param bucket_name:
        :param key:
        :param data:
        :param content_type:
        :return:

        eg
            put_object(bucket_name, key, open(filepath, 'rb'))
        """
        try:
            bucket = oss2.Bucket(self.auth, self.endpoint, bucket_name)
            result = bucket.put_object(key, data, headers=headers,
                                       progress_callback=progress_callback)
            if result.status == 200:
                return f'https://{bucket_name}.{self.endpoint}/{key}'
            else:
                return None
        except BaseException as e:
            return None


# def put_object_from_url(bucket_name, key, url):
#     """
#     上url地址流到aliyun
#     :param bucket_name:
#     :param key:
#     :param url:
#     :return:
#     """
#     try:
#         bucket = oss2.Bucket(auth, endpoint, bucket_name)
#         input = requests.get(url)
#         result = bucket.put_object(key, input, headers={
#             'Content-Type': input.headers['Content-Type']})
#         if result.status == 200:
#             return 'http://%s/%s' % (bucket_name.replace('-', '.'), key)
#         else:
#             return None
#     except BaseException as e:
#         print(e)
#         return None
#     pass
#
#
# def put_object_from_file(bucket_name, key, file_path):
#     """
#     上传文件
#     :param bucket_name:
#     :param key:
#     :param file_path:
#     :return:
#     """
#     try:
#         bucket = oss2.Bucket(auth, endpoint, bucket_name)
#         result = bucket.put_object_from_file(key, file_path)
#         if result.status == 200:
#             return 'http://%s/%s' % (bucket_name.replace('-', '.'), key)
#         else:
#             return None
#     except IOError as e:
#         print('IOError', e)
#         return None
#     pass


if __name__ == '__main__':
    oss = OSSClient()
    name = 'test/{}.json'.format(datetime.utcnow().timestamp())
    url = oss.put_object(BUCKET_IMG, name, '{"id":1}')
    print(url)

    pass
