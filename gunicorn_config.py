#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
配置信息
https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import multiprocessing

bind = '0.0.0.0:8002'
print(multiprocessing.cpu_count())
workers = 2  # multiprocessing.cpu_count() * 2 + 1  # 4  #
accesslog = 'access.log'
logconfig = 'gunicorn_logging.conf'
