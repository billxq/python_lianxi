#!/usr/bin/env python
# coding:utf-8
import shutil
from datetime import datetime

class CutLog(object):
	def __init__(self):
		self.accesslog = 'access.log'
		self.errorlog = 'error.log'

	def getToday(self):
		self.nowTime = datetime.now().strftime("%Y-%m-%d")
		self.todayAccesslog = self.nowTime + self.accesslog
		self.todayErrorlog = self.nowTime + self.errorlog

	def logRename(self):
		shutil.copy(self.accesslog,self.todayAccesslog)
		shutil.copy(self.errorlog,self.todayErrorlog)
		fa = open(self.accesslog,'w')
		fe = open(self.errorlog,'w')
		fa.close()
		fe.close()

def main():
	cutlog = CutLog()
	cutlog.getToday()
	cutlog.logRename()

if __name__ == "__main__":
	main()
