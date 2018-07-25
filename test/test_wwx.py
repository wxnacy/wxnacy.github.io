#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import sys
sys.path.append('~/Projects/wwx/wwx/models.py')
print(sys.path)
from models import Message



if __name__ == "__main__":
    msg = Message()
    msg.test()
