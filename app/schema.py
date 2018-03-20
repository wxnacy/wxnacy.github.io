#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from app.config import logger
from app.models import Code as CodeModel

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy import SQLAlchemyConnectionField

import graphene
from graphene import relay
from graphene.types.scalars import MIN_INT, MAX_INT
from graphql.language.ast import BooleanValue, StringValue, IntValue, ListValue, ObjectValue, FloatValue

from sqlalchemy import desc
from sqlalchemy import or_
from sqlalchemy import text

from datetime import datetime
from datetime import date


class JSON(graphene.Scalar):
    """
    The `JSON` scalar type represents JSON values as specified by
    [ECMA-404](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf).
    """

    @staticmethod
    def identity(value):
        logger.debug('JSON {}'.format(value))
        if isinstance(value, (str, bool, int, float)):
            return value.__class__(value)
        elif isinstance(value, (list, dict)):
            return value
        else:
            return None

    serialize = identity
    parse_value = identity

    @staticmethod
    def parse_literal(ast):
        logger.debug('JSON {}'.format(ast))
        if isinstance(ast, (StringValue, BooleanValue)):
            return ast.value
        elif isinstance(ast, IntValue):
            num = int(ast.value)
            return num
        elif isinstance(ast, FloatValue):
            return float(ast.value)
        elif isinstance(ast, ListValue):
            return [JSON.parse_literal(value) for value in ast.values]
        elif isinstance(ast, ObjectValue):
            return {field.name.value: JSON.parse_literal(field.value) for field in ast.fields}
        else:
            return None

    #  def __getattr__(self, key):
        #  return self[key]
    #  def __getitem__(self, key):
        #  return self[key]



class ActiveSQLAlchemyObjectType(SQLAlchemyObjectType):
    class Meta:
        abstract = True

    ext_property = graphene.Field(JSON)

    @classmethod
    def get_model(cls):
        return cls._meta.model

    @classmethod
    def query_item(cls, info, **kwargs):
        params = dict(is_available = 1)
        params.update(kwargs)
        m = cls.get_model()
        return cls.get_query(info).filter_by(**params).order_by(
            desc(m.create_ts)).first()

    @classmethod
    def query_items(cls, info, **kwargs):
        params = dict(is_available = 1)
        params.update(kwargs)
        m = cls.get_model()
        return cls.get_query(info).filter_by(**params).order_by(
            desc(m.create_ts)).all()

    @classmethod
    def query_count(cls, info, **kwargs):
        params = dict(is_available = 1)
        params.update(kwargs)
        return cls.get_query(info).filter_by(**params).count()

    @classmethod
    def query_by_id(cls, info, id):
        params = dict(is_available = 1, id=id)
        return cls.get_query(info).filter_by(**params).first()


class Code(ActiveSQLAlchemyObjectType):
    class Meta:
        model = CodeModel

class Query(graphene.ObjectType):
    code = graphene.Field(Code,
        description="获取 code",
        id = graphene.String()
    )

    test = graphene.Field(JSON)

    def resolve_test(self, info):
        return dict(name='wxnacy', age=1222222, l = [dict(name='ss')])

    def resolve_code(self, info, **args):
        return Code.query_item(info, **args)

schema = graphene.Schema(
    query=Query,
    # https://github.com/graphql-python/graphene/blob/master/docs/types/schema.rst#auto-camelcase-field-names
    auto_camelcase=False,               # 禁止自动转驼峰命名
)

