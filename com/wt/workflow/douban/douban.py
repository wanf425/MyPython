#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日

@author: wangtao
'''

import sys
import web
from workflow import Workflow, ICON_WEB
# from workflow import Workflow, ICON_WEB, web

def main(wf):
    url = 'https://api.douban.com/v2/book/search'
    params = dict(q=wf.args[0],count=20,format='json')
    r = web.get(url, params)
    r.raise_for_status()
    for post in r.json()['books']:
        authors = ''
        for author in post['author']:
            authors += author + ''
        detail = u'作者：' + author + u'|出版社：' + post['publisher'] + u'|价格：' + post['price'] + u'|评分：' + post['rating']['average']
        wf.add_item(post['title'], detail, arg=post['id'],
                    uid=post['id'], valid=True, icon=ICON_WEB)
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.argv.append(u'天命不足畏')
    sys.exit(wf.run(main))


