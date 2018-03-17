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
from app.models import Test
from app.config import db
from sqlalchemy import text

def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    for i in range(10):
        Test.create()
    db.session.commit()
    sql = 'select * from auto_id'
    res = db.engine.execute(text(sql)).fetchall()
    print(res)

