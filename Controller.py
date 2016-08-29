#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 10
if a > 10:
	print u'a比10大'
elif a < 10:
    print u'a比10小'
else:
	print u'a等于10'

b=5
loop=0
while b>0:
	loop = loop + 1
	b = b - 1
print 'loop',loop

al = [1,2,3]
for x in al:
	print x