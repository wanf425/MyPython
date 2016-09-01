#!/usr/bin/env python
# -*- coding: utf-8 -*-

# function as param
def f(x, y):
	return x + y

def ff(x, y, f):
	return f(x, y)

f1 = f
print 'function as param', ff(1, 2, f1)

# map/reduce
def mfun(x):
	return x * x

aList = [1, 2, 3, 4, 5, 6]
print 'map function', map(mfun, aList)

def refun(x, y):
	return x * y

print 'reduce function', reduce(refun, aList)


	
