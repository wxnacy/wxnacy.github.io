#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import hashlib
import sys
import inspect
import importlib
import os
import ast
import pickle
from app.models import AutoId
from app.models import Code

def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

a = 1 << 8
b = 1 << 8
c = 1 << 35
print(c)
print((a << 44) + (b << 36) + c)

res = AutoId.generate_id()
print(res)
Code.create(name='test')
