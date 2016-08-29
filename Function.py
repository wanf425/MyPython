#!/usr/bin/env python
# -*- coding: utf-8 -*-

#do function
print 'cmp 1 , 2,result:',cmp(1,2)
c = cmp
print 'c 1 , 2,result:',c(1,2)

#define function
def min(n1,n2=4):
	if n1 < n2:
		print 'n1 is less than n2'
	elif n1 > n2: 
		print 'n1 is more than n2'
	else: 
	    print 'n1 is equal n2'

min(5)

#multi return
def multireturn():
	return '1','2'

r = multireturn();
print 'multireturn',r

#dynimic param
def dynimicParam(*p1):
	for p in p1:
		print 'dynimic param',p

p = [1,2,3]
dynimicParam(*p)

#key param
def keyParam(**k1):
	for k in k1:
		print 'key param',k

keyParam(k1='value1',k2='value2')