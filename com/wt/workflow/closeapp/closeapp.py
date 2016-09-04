#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月3日

@author: wangtao
'''

import psutil

def killProcess():

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['username', 'name','status'])
            if pinfo['username'] == 'wangtao':
                print pinfo 
                print 'environ:',proc.environ()
        except psutil.NoSuchProcess,pid:
            print "no process found with pid=%s"%(pid)
            
if __name__ == '__main__':
    killProcess()