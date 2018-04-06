#!/usr/bin/env python
# coding:utf-8
import requests
import re

class GetMag(object):
	def __init__(self):
		self.res = None
		self.mag = None
	def getText(self,url):
		self.res = requests.get(url).text
	def getMag(self):
		pat = re.compile(r'''data-magnet="(.*?)"''')
		self.mag = re.findall(pat,self.res)
		print(self.mag)


def main():
	getmag = GetMag()
	getmag.getText(url='http://oabt004.com/index/index?cid=1')
	getmag.getMag()

if __name__ == "__main__":
	main()
