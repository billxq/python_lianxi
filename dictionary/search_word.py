#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/30 上午10:25
# @author: Bill
# @file: search_word.py.py
from sqlalchemy.orm import sessionmaker

from dictionary.create_tb import *
from dictionary.write_to_db import Dictionary

engine = CreateTable().getEngine()
DBsessoin = sessionmaker(bind=engine)
session = DBsessoin()

word = input("Please input a word you want to search: ")


result = session.query(Dictionary).filter(Dictionary.key == f'{word}').all()
for res in result:
    print(res.value)