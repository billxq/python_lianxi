#!/usr/bin/env python
# coding:utf-8
# @author: Bill
# @time: 2018-06-01

import socket
import threading
import subprocess

ss = socket.socket()

host = socket.gethostname()
port = 9999


ss.bind((host,port))
ss.listen(5)

def getCmd(sock,addr):
    while 1:
        data = sock.recv(1024)
        if not data or str(data,'utf8') == "exit":
            break
        cmd = str(data,'utf8')
        results = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        result = results.stdout.read()  # result是命令执行的结果，bytes类型
        result_len = len(result)
        sock.send(bytes(str(result_len),"utf8"))    # 有时候命令结果一次超过1024，所以要把命令结果的长度发送给客户端，比较长度
        sock.sendall(result)    # 发送命令执行的结果
    sock.close()

while 1:
    sock,addr = ss.accept()
    t = threading.Thread(target=getCmd,args=(sock,addr))
    t.start()