#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 切片
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print '1 to 3', alist[0:3]
print '3 to 5', alist[2:5]
print u'倒数第4个到倒数第2个', alist[-5:-2]
print '1 to 10,per 3', alist[0:10:3]

# 迭代
for i, v in enumerate(alist):
	print i, v

adict = {'k1':1, 'k2':2, 'k3':3}
for k, v in adict.iteritems():
	print k, v

# 列表生成式
print [x * x for x in range(1, 10) if x % 2 == 0]

# 生成器
g = (x * x for x in range(1, 10) if x % 2 == 0)

for x in g:
	print x

def fib(maxv):
	n, a, b = 0, 0, 1
	while n < maxv:
		yield b
		a, b = b, a + b
		n = n + 1

f = fib(6)
for x in f:
	print x
	
