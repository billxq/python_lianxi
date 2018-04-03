#!/usr/bin/env python
# coding:utf-8

class GetList(object):
	def __init__(self):
		print("This class is set to sort the list!")
		self.data = self.get_data()
		self.L = self.str_to_intlist(self.data)
	def get_data(self):
		data = input("Please input a list(eg.12,34,56,78): ")
		result = self.is_ok(data)
		if result:
			return data
		else:
			print("What you input is wrong! Please look at the example!")
			exit(1)
	def is_ok(self,data):
		valid_list = ['0','1','2','3','4','5','6','7','8','9',' ',',']
		result = True
		for i in data:
			if i not in valid_list:
				result = False 
				return result
		return result
	def str_to_intlist(self,data):
		L = list()
		for i in data.split(','):
			if i.strip().isdigit():
				L.append(int(i.strip()))
		return L

class Bubble(GetList):
	def __init__(self):
		super(Bubble,self).__init__()
		self.sortList(self.L)
	def sortList(self,list):
		for i in range(0,len(list)):
			for j in range(i,len(list)):
				if list[i] > list[j]:
					a  = list[i]
					list[i] = list[j]
					list[j] = a
		print(list)
		
if __name__ == '__main__':
	bubble = Bubble()

