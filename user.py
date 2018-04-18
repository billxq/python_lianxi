#!/usr/bin/env python
# coding:utf-8

class User(object):
    def __init__(self,first,last,**kwargs):
        self.first = first
        self.last = last
        self.infos = kwargs
    def describe_user(self):
        profile = dict()
        profile['First name'] = self.first
        profile['Last name'] = self.last
        for k,v in self.infos.items():
            profile[k] = v
        print(profile)
    def greet_user(self):
        print("Hello,{} {}".format(self.first,self.last))

user = User('Xu','Qing',Age=18,Gender='Male',Job='Teacher')
user.describe_user()
user.greet_user()
