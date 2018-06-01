#!/usr/bin/env python
# coding:utf-8

import subprocess

a = subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
print(a)
print(a.stdout.read().decode("utf8"))