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

    def __repr__(self):
        return 'räpr'

    def __format__(self, fmt):
        if fmt == 'fmt':
            return "I'm format user"
        return 'user'

if __name__ == "__main__":
    u = User()
    print('{:fmt}'.format(u))
    print('{!s}'.format(u))
    print('{!r}'.format(u))
    print('{!a}'.format(u))
