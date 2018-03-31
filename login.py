#!/usr/bin/env python
# coding:utf-8

import codecs
user_dict = dict()
with codecs.open('user.txt','r') as f:
    contents = f.readlines()
for content in contents:
    content = content.strip('\n')
    user = content.split(':')[0]
    password = content.split(':')[1]
    user_dict.update({user:password})

with codecs.open('fail_login.txt') as f:
    banned_user = [i.strip('\n') for i in f.readlines()]
#print(banned_user)    

fail_count = 0
user = input(u"请输入用户名： ")
while 1:
    if user in banned_user:
        print("该用户已被锁定！")
        exit(1)
    if user in user_dict.keys():
        password = input(u"请输入密码： ")
        if password == user_dict.get(user):
            print("{},欢迎登陆！".format(user))
            exit(1)
        else:
            print("密码输入错误，请重新输入！")
            fail_count += 1
        if fail_count == 3:
            with codecs.open('fail_login.txt','a') as f:
                f.write(user)
                f.write("\n")
            print("超过尝试次数，用户名被锁定！")
            exit(1)
    else:
        print('用户{}没有注册，请先注册！'.format(user))
        exit(1)
