#!/usr/bin/env python
# coding:utf-8

import pymysql

def db_connect():
    db_config = {
        "host":"10.148.60.26",
        "port":3306,
        "user":"python",
        "passwd":"123456",
        "db":"python" 
    }
    db = pymysql.connect(**db_config)
    return db


def create_table():
    db = db_connect()
    cur = db.cursor()
    cur.execute("drop table if exists STUDENT;")
    sql = """create table STUDENT(
            Name char(20) not null,
            Age int,
            Gender enum("Male","Female"),
            STUID int
    )"""
    try:
        cur.execute(sql)
        db.commit()
        print("Create Table Success!")
    except Exception as e:
        db.rollback()
        print("Create Table Failure.")
        print(e)
    finally:
        db.close()

def insert_data():
    db  = db_connect()
    cur = db.cursor()
    sql = """insert into STUDENT(Name,Age,Gender,STUID)
            values("Bill",18,"Male",001)"""
    try:
        cur.execute(sql)
        db.commit()
        print("Success")
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()

def query_data():
    db  = db_connect()
    cur = db.cursor()
    sql = """select * from STUDENT where STUID = 1;"""
    try:
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            print(f"Name:{row[0]}")
            print(f"Age:{row[1]}")
            print(f"Gender:{row[2]}")
            print(f"Studentid:{row[3]}")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()
        

if __name__ == "__main__":
    create_table()
    insert_data()
    query_data()
