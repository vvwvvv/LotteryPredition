#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-20 22:13:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import json
import urllib.request
import time


class LotteryBook(object):
	"""docstring for LotteryBook"""
	

	def __init__(self,path='./data/data.json'):
		super(LotteryBook, self).__init__()
		self.data = self.read_json(path)
		self.newest_lottry_list = self.get_newest_lottry_list()
		pass


	def get_current_date(self):
		return time.strftime("%Y%m%d")

	def read_json(self,path):
		with open(path,"r") as f:
			return json.load(f)
	def write_json(self,path):
		with open(path,"w") as f:
			json.dump(self.data,f )

	def get_newest_lottry_list(self):
		# print([self.data[1][k]  for k in sorted(self.data[1])])
		return [self.data[0][-1][0],
			self.data[1][self.data[0][-1][0][:4]][1]]
	def get_order_list(self,*nper):
		nper = [str(np) for np in nper]
		try:

			if len(nper) == 1:
				if len(nper[0]) == 4:
					if nper[0] in self.data[1].keys():
						order = self.data[1][nper[0]]
						return order
					else:
						raise ValueError('year is not in datebase')
				elif len(nper[0]) == 7:
					base = self.get_order_list(nper[0][:4])
					if base[:6] == 'error:':
						return base
					order = int(base[0])+int(nper[0][4:])-1
					if order <= int (base[1]) :
						return [str(order)]
					else :

						raise ValueError('nper out of range')
				else :
					raise ValueError('the nper length must be 4 or 7')
			elif len(nper) == 2 and int(nper[0][:4])<int(nper[1][:4]) :
				order = self.get_order_list(nper[0])
				if order[:6] == 'error:':
						return order
				if len(order) == 1: 
					order.append('')
				order[1]= self.get_order_list(nper[-1])
				if order[1][:6] == 'error:':
						return order[1]
				order[1]=order[1][-1]
				return order
			else :
				raise ValueError('arg count is not 1 or 2,or the order is wrong')
		except Exception as e :
			return('error:'+str(e))
			pass
		finally:
			pass
			
		

if __name__ == '__main__':
	foo = LotteryBook()
	print(foo.get_order_list(2003005,2014))

