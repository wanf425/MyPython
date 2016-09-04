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
    d = Douban(wf)
    d.doSearch()
    
class Douban(object):
    def __init__(self, workflow):
        self.__search_type = workflow.args[0]
        self.__args = workflow.args[1:]
        self.__workflow = workflow
        
    def doSearch(self): 
        url = self.__geturl()
        params = self.__getparams(self.__args)
        r = web.get(url, params)
        r.raise_for_status()
        self.__addWorkflowItems(r)
        self.__workflow.send_feedback()
        
    def __addWorkflowItems(self, r):
        json = r.json()
        
        if self.__search_type == Constants.SEARCH_TYPE_MUSIC:
            for post in json['musics']:
                attrs = post['attrs']
                title = self.__getinfo(attrs['title'])
                singer = ''
                publisher = ''
                pubdate = ''
                version = ''
                
                postid = post['id']
                
                if attrs.has_key('singer'): singer = self.__getinfo(attrs['singer'])
                if attrs.has_key('publisher'): publisher = self.__getinfo(attrs['publisher'])  
                if attrs.has_key('pubdate'): pubdate = self.__getinfo(attrs['pubdate'])          
                if attrs.has_key('version'): version = self.__getinfo(attrs['version'])
                   
                detail = u'%s / %s / %s / %s' % (singer, publisher, pubdate, version) 
                self.__workflow.add_item(title, detail, arg=postid , uid=postid, valid=True, icon=ICON_WEB)
        elif self.__search_type == Constants.SEARCH_TYPE_MOVIE:
            for post in json['subjects']:
                postid = post['id']
                rating = post['rating']['average']
                title = post['title']
#                 director = post['directors']['name']
                director = ''
                detail = u'%s / %s ' % (rating, director) 
                self.__workflow.add_item(title, detail, arg=postid , uid=postid, valid=True, icon=ICON_WEB)
        else:
            for post in json['books']:
                authors = self.__getinfo(post['author'])
                detail = u'%s / %s / %s / %s' % (authors, post['publisher'], post['price'], post['rating']['average']) 
                self.__workflow.add_item(post['title'], detail, arg=post['id'], uid=post['id'], valid=True, icon=ICON_WEB)
    
    def __getinfo(self,infos):
        result = ''
        if infos:
            for info in infos:
                result += info + ' '
        
        return result
       
    def __geturl(self):
        if self.__search_type == Constants.SEARCH_TYPE_MUSIC:
            return Constants.URL_MUSIC_SEARCH
        elif self.__search_type == Constants.SEARCH_TYPE_MOVIE:
            return Constants.URL_MOVIE_SEARCH
        else:
            return Constants.URL_BOOK_SEARCH
        
    def __getparams(self, args):
        if self.__search_type == Constants.SEARCH_TYPE_MUSIC:
            return dict(q=args[0], count=20)
        elif self.__search_type == Constants.SEARCH_TYPE_MOVIE:
            return dict(q=args[0], count=20)
        else:
            return dict(q=args[0], count=20)
        
class Constants(object):
    SAERCH_TYPE_BOOK = 'book'
    SEARCH_TYPE_MUSIC = 'music'
    SEARCH_TYPE_MOVIE = 'movie'
    
    URL_BOOK_SEARCH = 'https://api.douban.com/v2/book/search'
    URL_MUSIC_SEARCH = 'https://api.douban.com/v2/music/search'
    URL_MOVIE_SEARCH = 'https://api.douban.com/v2/movie/search'
    
if __name__ == u"__main__":
    wf = Workflow()
    sys.argv.append('movie')
    sys.argv.append('星球大战')
#     sys.argv.append('music')
#     sys.argv.append('千里之外')
#     sys.argv.append('book')
#     sys.argv.append(u'天命不足畏')
    sys.exit(wf.run(main))


