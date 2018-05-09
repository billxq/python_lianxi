#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @date: 2018/5/9 上午9:41
# @author: Bill
# @file: demon1.py

import multiprocessing
import os
import time

# def pro_test(name):
#     print("Run child process {},pid={}".format(name,os.getpid()))
#
# if __name__ == '__main__':
#     print("Parent process {} ".format(os.getpid()))
#     p = multiprocessing.Process(target=pro_test,args=('test',))
#     p.start()
#     p.join()
#     print("Child process end!")

# def work(interval, method):
#     print("start work_" + method)
#     time.sleep(interval)
#     print("end work_" + method)
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=work,args=(1,'1'))
#     p2 = multiprocessing.Process(target=work,args=(2,'2'))
#     p3 = multiprocessing.Process(target=work,args=(3,'3'))
#     p1.start()
#     p2.start()
#     p3.start()
#     print(f"The number of CPU is {multiprocessing.cpu_count()}")
#     for p in multiprocessing.active_children():
#         print(f'The name of active child is {p.name}. Pid is {p.pid}. This pid is alive or not:{p.is_alive()}')
#     print('END!')

# def lock_with(lock,f):
#     with lock:
#         fs = open(f,'w')
#         fs.write('Lock acquired via with' + '\n')
#         fs.close()
#
# def lock_acquire(lock,f):
#     lock.acquire()
#     try:
#         fs = open(f,'a')
#         fs.write('lock acquired via acquire' + '\n')
#         fs.close()
#     finally:
#         lock.release()
#
#
# if __name__ == '__main__':
#     f = 'test.txt'
#     lock = multiprocessing.Lock()
#     pw = multiprocessing.Process(target=lock_with,args=(lock,f))
#     pa = multiprocessing.Process(target=lock_acquire,args=(lock,f))
#     pw.start()
#     pa.start()
#     print('Main end')

# def add1(lock,val,num):
#     with lock:
#         print("The initial number is {}".format(num))
#         for i in range(1,5):
#             num += val
#             time.sleep(0.3)
#             print("The number is {}".format(num))
#
# def add3(lock,val,num):
#     lock.acquire()
#     print("The initial number is {}".format(num))
#     try:
#         for i in range(1,5):
#             num += val
#             time.sleep(0.3)
#             print("The number is {}".format(num))
#     finally:
#         lock.release()
def add1(val,num):
    print("The initial number is {}".format(num.value))
    for i in range(1,5):
        num.value += val
        time.sleep(0.3)
        print("The number is {}".format(num.value))

def add3(val,num):
    print("The initial number is {}".format(num.value))
    for i in range(1,5):
        num.value += val
        time.sleep(0.3)
        print("The number is {}".format(num.value))

if __name__ == '__main__':
    # lock = multiprocessing.Lock()
    num = multiprocessing.Value('i',0)
    p1 = multiprocessing.Process(target=add1,args=(1,num))
    p3 = multiprocessing.Process(target=add1,args=(3,num))
    p1.start()
    p3.start()
    print("Main process end!")
