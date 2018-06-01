#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/30 上午8:58
# @author: Bill
# @file: write_to_db.py
import codecs

from sqlalchemy.orm import sessionmaker

from dictionary.create_tb import *


class Dictionary(Base):
    __tablename__ = 'dictionary'
    id = Column(Integer,primary_key=True)
    key = Column(String(50))
    value = Column(String(50))


class WriteToDB(object):
    def __init__(self):
        engine = CreateTable().getEngine()
        DBsessoin = sessionmaker(bind=engine)
        self.session = DBsessoin()

    def writeData(self,filename):
        with codecs.open(filename,'r',encoding="utf-8") as f:
            for num, content in enumerate(f.readlines()):
                key = content.strip().split()[0]
                value = content.strip().split()[1]
                dictionary = Dictionary(id=num+1,key=key,value=value)
                self.session.add(dictionary)
            self.session.commit()
            self.session.close()


# writetodb = WriteToDB()
# writetodb.writeData('dictionary.txt')
