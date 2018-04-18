#!/usr/bin/env python
# coding:utf-8

def userProfile(first,last,**infos):
	profile = dict()
	profile['first name'] = first
	profile['last name']  = last
	for k,v in infos.items():
		profile[k] = v
	return profile

profile = userProfile('Xu','Bill',Age=18,Gender='Male',Job='Teacher')
print(profile)
