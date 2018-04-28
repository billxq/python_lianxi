#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/4/28 上午8:48
# @author: Bill
# @file: alchemy.py

# from sqlalchemy import create_engine, MetaData, Integer, Table, Column, String
# from sqlalchemy.orm import sessionmaker



# cursor = engine.connect()
# sql = """
#     create table if not exists student(
#     id int not null primary key,
#     name varchar(100),
#     age int,
#     address varchar(100)
#     )ENGINE=INNODB DEFAULT charset=utf8 auto_increment=1;
# """
# cursor.execute(sql)
# cursor.close()

# metadata = MetaData(engine)
# user = Table("user",metadata,
#              Column('id',Integer,primary_key=True),
#              Column('name',String(100)),
#              Column('age',Integer)
#              )
# metadata.create_all(engine)



from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query

Base = declarative_base()
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    address = Column(String(100))

engine = create_engine("mysql+pymysql://alchemy:123456@fishxq.gicp.net/sqlalchemy",echo=False)
DBsession = sessionmaker(bind=engine)
session = DBsession()
# new_student = Student(id=10001, name="Bill", age=18,address='Xumin Rd 111')
# new_student2 = Student(id=10002, name="Tom", age=18,address='Xumin Rd 112')
# new_student3 = Student(id=10003, name="Floria", age=18, address='Xumin Rd 113')
# new_student4 = Student(id=10004, name="Carrie", age=18, address='Xumin Rd 114')
# session.add(new_student)
# session.add_all([new_student2, new_student3,new_student4])  # 可以把数据一次都插入但是参数为一个列表
# session.commit()
# session.close()
# student1 = session.query(Student).filter_by(name='Tom').first()
# print(student1.id,student1.name,student1.age,student1.address)
student2 = session.query(Student).filter(Student.name.like('%o%')).first()
print(student2.name)






