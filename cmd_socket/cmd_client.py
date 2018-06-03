#!/usr/bin/env python
# coding:utf-8
# @author: Bill
# @time: 2018-06-01

import socket

sc = socket.socket()

host = socket.gethostname()
port = 9999


sc.connect((host,port))

while 1:
    data = input(">>> ")
    if data == "exit":
        break
    sc.send(bytes(data,"utf-8"))    # 发送命令给服务端
    result_len = str(sc.recv(1024),"utf8")
    result = bytes()  # 初始化一个data，用于接收完整的命令结果
    while len(result) != int(result_len):
        result += sc.recv(1024)
    print(str(result,"gbk"))



sc.close()
