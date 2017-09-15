#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''公共需要run的项目'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common.base import BaseResponse
from app.config import BaseConfig
from app.config import app
from app.config import db
from app.models import Article

from flask_restless import APIManager
import traceback

# restful
URL_PREFIX = '/restful/v1' # BaseConfig.APPLICATION_ROOT_RESTFUL
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Article, url_prefix=URL_PREFIX, methods=['GET','POST'])


@app.errorhandler(Exception)
def app_error_handler(e):
    app.logger.error(traceback.format_exc())
    return BaseResponse.return_internal_server_error(str(e))
