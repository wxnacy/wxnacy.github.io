#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from app.config import db
from app.models import VisitorLogDate
from app.models import VisitorLog


if __name__ == "__main__":
    VisitorLogDate.statistics_visitor()
    item = VisitorLog.query_item(id=68719477613)
    print(item.md5)
    print(VisitorLog.md5)
    print(VisitorLog.id)
