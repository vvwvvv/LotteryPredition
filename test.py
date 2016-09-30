#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-19 22:37:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# with open("./all.txt","r") as f:
# 	data = f.readlines()
# 	data.reverse()
# with open("./data/2003001*2015031.txt","w") as f:
# 	f.write(''.join(data))
# 	pass

import json

with open("./data/bak/2003001*2015031.txt","r") as f:
	data = f.readlines()
	lottry_list =[]
	year_index_dict={}
	newdata = [lottry_list,year_index_dict]
	for idx,lottry in enumerate(data):
		lottry = lottry.split()
		lottry_list.append(lottry)
		year = lottry[0][:4]
		if year not in year_index_dict.keys():
			year_index_dict[year] = [str(idx+1),str(idx+1)]
			# print(type(year))
			# print (type(int(lottry[0][:4])))
		else:
			year_index_dict[year][1] = str(idx+1)

	print (len(newdata[1]))

with open("./data/data.json","w") as f:
	print(help(json.dump))
	json.dump(newdata,f,sort_keys = True,indent =1 )
with open("./data/data.json","r") as f:
	fdata = json.load(f)
	print(fdata==newdata)
		
	# print(data[:10])