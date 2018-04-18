#!/usr/bin/env python
# coding:utf-8

class User(object):
    def __init__(self,first,last,**kwargs):
        self.first = first
        self.last = last
        self.infos = kwargs
        self.login_attempts = 0
    def describe_user(self):
        profile = dict()
        profile['First name'] = self.first
        profile['Last name'] = self.last
        for k,v in self.infos.items():
            profile[k] = v
        print(profile)
    def greet_user(self):
        print("Hello,{} {}".format(self.first,self.last))
    def reset_login_attempts(self):
        self.login_attempts = 0
    def increment_login_attempts(self):
        self.login_attempts += 1
user = User('Xu','Qing',Age=18,Gender='Male',Job='Teacher')
user.describe_user()
user.greet_user()
print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
