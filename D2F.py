#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-19 22:37:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

def AppendName(url,bak):
	newurl=list(os.path.splitext(url))
	newurl.insert(-1,str(bak))
	newurl="".join(newurl)
	return newurl
def ChangeName(url,name):
	path = os.path.split(url)[0]
	newname = str(name)+str(os.path.splitext(url)[-1])
	return (os.path.join(path,newname))

def ReadFile2List(url):
	with open (url,'r') as f:
		content =f.readlines()
	return content

def WriteList2File(url,content):
	with open (url,'w') as f:
		f.write("".join(content))
	return len(content)

def SplitList2dictByRange(li,f=0,l=4):
	keyworddict={}
	for content in li:
		keyword = content[f:l]
		a = content
		if keyword not in keyworddict.keys():
			keyworddict[keyword]=[]
		keyworddict[keyword].append(content)
	return keyworddict

def function(url,content):
	


def do (url):
	content = ReadFile2List(url)
	content.reverse()
	contentalldict = SplitList2dictByRange(content)
	print (contentalldict.keys())
	for year in sorted(contentalldict.keys()):
		print (year)
		contentsinglelist=contentalldict[year]
		newurl = ChangeName(url,str(year)+(str(len(contentsinglelist))).zfill(3))
		WriteList2File(newurl,contentsinglelist)
#do('./data/all.txt')

