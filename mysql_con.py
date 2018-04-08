#!/usr/bin/env python
# coding:utf-8

import pymysql

def conn_mysql():
	data = {
		"host":"127.0.0.1",
		"port":3306,
		"user":"python",
		"passwd":"123456",
		"db":"python"
	}
	conn = pymysql.connect(**data)
	return conn

print(conn_mysql())
