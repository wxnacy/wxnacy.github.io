#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''加密工具'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import logger
import base64
import hashlib
import xmltodict
import json
from enum import Enum
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from datetime import datetime




def sha1(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode("utf-8"))
    return sha1.hexdigest()

class AESecurity():
    @classmethod
    def generate_key(cls):
        return Md5.encrypt('{}'.format(time.time()))

    def __init__(self, key):
        self.key = key
        self.iv = key[:16]
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext).decode("utf-8")

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(text).decode("utf-8")
        return plain_text

class WXSecurity():

    def __init__(self, token = 'F3uIXPvYZ8nmpPVhazFkert',
            encoding_aes_key = 'F3uIXPvYZ8nmpPVhazFkertj25fry8OcINM87xRe4kg'):
         self.token = token
         self.encoding_aes_key = encoding_aes_key

    def check_request(self, signature, timestamp, nonce):
        '''检查请求是否复核加密'''
        data = [self.token, str(timestamp), str(nonce)]
        data.sort()
        sign = sha1(''.join(data))
        return sign == signature

    def get_security_body(self, msg_encrypt, msg_signature, timestamp, nonce):
        '''获取加密消息体'''
        check_data = [self.token, msg_encrypt, timestamp, nonce]
        check_data.sort()
        sign = sha1(''.join(check_data))
        if sign == msg_signature:
            try:

                aes_key = base64.b64decode(f'{self.encoding_aes_key}=')
                aes = AESecurity(aes_key)
                aes_msg = base64.b64decode(msg_encrypt)
                body = aes.decrypt(aes_msg)
                print(body)

                pad = ord(body[-1])
                print(pad)
                return 200, body[20:-21]
            except Exception as e:
                print(e)
                return 500, '加密信息解析失败'
        else:
            return 500, '加密校验失败'

class Message():
    class MsgType(Enum):
        text = 'text'
        news = 'news'
        event = 'event'
        image = 'image'
        voice = 'voice'
        video = 'video'
        location = 'location'
        link = 'link'
        tcs = 'transfer_customer_service'

    class EventType(Enum):
        media_overseas = 'media_overseas'
        media_tomorrow = 'media_tomorrow'
        media_recommend = 'media_recommend'

    class Event(Enum):
        subscribe = 'subscribe'
        unsubscribe = 'unsubscribe'
        click = 'CLICK'
        view = 'VIEW'
        location = 'LOCATION'
        SCAN = 'SCAN'

    def __init__(self, xml_input):
        self.msg = json.loads(json.dumps(xmltodict.parse(xml_input)))
        data = self.msg['xml']
        self.owner_id = data['ToUserName']
        self.sender_id = data['FromUserName']
        self.msg_type = data['MsgType']

        self.event = data.get('Event')
        self.event_key = data.get('EventKey')
        # 用户发送消息给公众号会产生的字段
        self.msg_id = data.get('MsgId')
        self.content = data.get('Content')
        self.pic_url = data.get('PicUrl')
        self.media_id = data.get('MediaId')
        self.thumb_media_id = data.get('ThumbMediaId')
        self.media_format = data.get('Format')  # amr speex
        self.location_x = data.get('Location_X')
        self.location_y = data.get('Location_Y')
        self.scale = data.get('Scale')  # 缩放范围
        self.label = data.get('Label')  # 地理位置
        self.title = data.get('Title')
        self.description = data.get('Description')
        self.url = data.get('Url')
        # 用户点击菜单会产生的字段
        self.latitude = data.get('Latitude')
        self.longitude = data.get('Longitude')
        self.precision = data.get('Precision')  # 位置精度

    def is_text(self):
        return self.msg_type == self.MsgType.text.value

    def is_event(self):
        return self.msg_type == self.MsgType.event.value

    def is_image(self):
        return self.msg_type == self.MsgType.image.value

    def is_video(self):
        return self.msg_type == self.MsgType.video.value

    def reply_text(self, content):
        """回复文本"""
        return self._generator_reply(content)

    def reply_tcs(self):
        """转发客服"""
        return self._generator_reply(msg_type=self.MsgType.tcs.value)

    def reply_news(self, news):
        """回复图文消息"""
        return self._generator_reply(msg_type=self.MsgType.news.value,
                                     news=news)

    def reply_image(self, media_id):
        """回复图片"""
        return self._generator_reply(msg_type=self.MsgType.image.value,
                                     media_id=media_id)

    def reply_video(self, media_id):
        """回复视频"""
        return self._generator_reply(msg_type=self.MsgType.video.value,
                                     media_id=media_id)

    def make_news(self, data):
        return [self.News(**o).to_dict() for o in data]

    def get_user(self):
        """获取用户信息"""

        pass

    def _generator_reply(self, *args, **kwargs):
        content = args[0] if args else kwargs.get('content')
        msg_type = kwargs.get('msg_type') or self.MsgType.text.value

        xml = dict(
            ToUserName=self.sender_id,
            FromUserName=self.owner_id,
            CreateTime=int(datetime.now().timestamp()),
            MsgType=msg_type
        )

        if msg_type == self.MsgType.text.value:
            xml['Content'] = content
        elif msg_type == self.MsgType.news.value:
            items = kwargs.get('news')
            xml['Articles'] = dict(item=items)
            xml['ArticleCount'] = len(items)
        elif msg_type == self.MsgType.image.value:
            xml['Image'] = dict(MediaId=kwargs.get('media_id'))
        elif msg_type == self.MsgType.video.value:
            xml['Video'] = dict(MediaId=kwargs.get('media_id'))

        return xmltodict.unparse({"xml": xml})

    @classmethod
    def decrypt_body(cls, xml_input, msg_signature, timestamp, nonce):
        msg = json.loads(json.dumps(xmltodict.parse(xml_input)))
        data = msg['xml']
        encrypt = data['Encrypt']
        wxs = WXSecurity()
        return wxs.get_security_body(encrypt, msg_signature, timestamp, nonce)



EAKEY = 'F3uIXPvYZ8nmpPVhazFkertj25fry8OcINM87xRe4kg'
token = 'F3uIXPvYZ8nmpPVhazFkert'
ts ='1531971200'
nonce = '1278028470'
signature = '088af82e460f44ac5b9e3acc8b82dac6d329de54'
encrypt = 'S6eEBV46zgL6+m2SXqBWXCbDnxuPI7Eca4Yoj0IXlvFuWqCPXey7IzSzyKHZc5Gbz5ODSyycSy1vsEvT8zc/bU73KHugVOQzBd/MFbgiYJ/vzZ1vPXdQUUIIMbSV7MTrtXCNHBPKacyawsPVnhqxiYZpBEbwXBVvOIse5hFnSkYIrWmcD1xv1SS4kH93ndnOY8KamohUNVBUzNuDbCUwaNuVrmPljYG+EskwjKVT262sWwcfHtdb4hriZAswbu4cK77QzvmtijHnfQP2+bLoVY4hvPU0zgmIbz64yQjma8pEdWtNZS8/raFyuW6C4Ns7GhcS21qXSAFLDpwiaKYSxEnu8q6UfgFeQ1xgxaRb6amhRz51hIjw2IhGXuVL6+xnaCASHftHQXmyeO/udLXe0+vChqkBg+Uy69FoSRFtNd4='
msg_s = '9f3178c8b6e445a0b2af112d0425c2972ffca176'

if __name__ == "__main__":
    print(f'{EAKEY}=')
    key = base64.b64decode(f'{EAKEY}=')
    #  print(key)
    #  print(len(key))
    aes = AESecurity(key)
    s = aes.encrypt('test')
    #  print(s)
    #  t = aes.decrypt(s)
    #  print(t)
    #  print([token, ts, nonce].sort())

    wxs = WXSecurity(token, EAKEY)
    flag = wxs.check_request(signature, ts, nonce)
    s, res = wxs.get_security_body(encrypt, msg_s, ts, nonce)
    msg = Message(res.encode())
    print(msg.content)
