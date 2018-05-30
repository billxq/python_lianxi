#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/30 上午8:32
# @author: Bill
# @file: create_tb.py
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CreateTable(object):
    def getEngine(self):
        self.engine = create_engine("mysql+pymysql://alchemy:123456@fishxq.gicp.net:6106/sqlalchemy?charset=utf8")
        return self.engine
    def createTb(self):
        # 创建一个表用于存储dictionary.txt中的数据
        metadata = MetaData(self.getEngine())
        dictionary_tbconfig = Table("dictionary", metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('key', String(50)),
                                    Column('value', String(50))
                                    )
        metadata.create_all(self.getEngine())



create_table = CreateTable()
create_table.createTb()
