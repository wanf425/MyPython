#!/usr/bin/env python
# -*- coding: utf-8 -*-

#list
alist = [1,'2',['3','4']]
print 'alist',alist
print 'length',len(alist)
print 'index 1 value',alist[1]
print 'last value',alist[-1]
print 'append',alist.append(5)
print 'after append',alist
print 'insert',alist.insert(1,6)
print 'after insert',alist
print 'pop',alist.pop(1)
print 'after pop',alist	

p#tuple
atuple = (1,2,'3')
print atuple
atuple = (1,)
print atuple

#dict
adict = {'wt':20,'lff':19,'dc':18,10:17}
print 'adict',adict
print 'get key wt',adict['wt'] 
print 'key kdc is in adict', 'kdc' in adict

#set
aset = ([1,2,3])
print 'aset',aset
print 'index 1 value',aset[1]