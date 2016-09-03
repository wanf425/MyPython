#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日

@author: wangtao
'''

import sys
import web
from workflow import Workflow
# from workflow import Workflow, ICON_WEB, web

def main(wf):
    url = 'http://fanyi.youdao.com/openapi.do'
    params = dict(q=wf.args[0],keyfrom='PersonalAlfred',key='1030208618',type='data',doctype='json',version='1.1')

    r = web.get(url, params)
    r.raise_for_status()
    result = r.json()
    if result['errorCode'] == 0 and result.has_key('basic'):
        phonetic = ''
        if result['basic'].has_key('phonetic'):
            phonetic = result['basic']['phonetic']
            
        wf.add_item(result['basic']['explains'][0], phonetic , arg=result['query'],
                        uid=result['query'], valid=True, icon="youdao.png")
        wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.argv.append('ww')
    sys.exit(wf.run(main))


