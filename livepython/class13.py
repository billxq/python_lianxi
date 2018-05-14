#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/14 下午12:55
# @author: Bill
# @file: class13.py

import pymysql
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext import declarative
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    address = Column(String(100))

def update(session):
    student1 = session.query(Student).filter(Student.id == 10001).one()
    student1.age = 20
    session.commit()
    student2 = session.query(Student).filter(Student.id == 10001).one()
    print(student2.age)

def delete(session):
    session.query(Student).filter(Student.id == 10001).delete()
    session.commit()

def count(session):
    numnber = session.query(Student).filter().count()
    print("total student is {0}".format(numnber))

def groupBy(session):
    groupByAge = session.query(Student).group_by(Student.age).all()
    print(groupByAge)
    for i in groupByAge:
        print(i.id, i.name, i.age, i.address)

def orderBy(session):
    orderByAge = session.query(Student).order_by(Student.age.desc()).all()
    for x in orderByAge:
        print(x.id, x.name, x.age, x.address)


def insert(session):
    new_student1 = Student(id=10001, name="Bill", age=18, address='Xumin Rd 111')
    new_student2 = Student(id=10002, name="Tom", age=18, address='Xumin Rd 112')
    new_student3 = Student(id=10003, name="Floria", age=18, address='Xumin Rd 113')
    new_student4 = Student(id=10004, name="Carrie", age=18, address='Xumin Rd 114')
    session.add_all([new_student1,new_student2,new_student3,new_student4])
    session.commit()

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://alchemy:123456@fishxq.gicp.net:6106/sqlalchemy',echo=True)
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    update(session)
