#!/usr/bin/env python
# -*- coding:utf-8 -*-

def makeSandwich(*toppings):
	print("Making the sandwich with the following toppings:")
	for topping in toppings:
		print("- " + topping)

makeSandwich('mushrooms','ketchups')
makeSandwich('mushrooms','ketchups','peppers')
makeSandwich('mushrooms','ketchups','sweets','extra cheese')
