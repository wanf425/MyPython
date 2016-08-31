#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年8月31日

@author: wangtao
'''
# 引入模块并定义别名
import com.wt.AdvanceFeatures as af

# 用try...expect...引入模块
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
    
af.fib(6)

# 定义私有方法，这个方法仍然是可以被外部模块直接调用的
def __private_fun():
    print 'this is a private function'

def public_fun():
    __private_fun()
    print 'this is a public function'

