#!/usr/bin/python

from collections import OrderedDict



def using_orderedict(li):
	a = list(OrderedDict.fromkeys(li))
	return a

def use_append(li):	
	b = []
	b = [ i for i in li if i not in b]
	return b

li = ['1','2',3,'4','2','1',5,6,9]

print using_orderedict(li)
print "b:",use_append(li)
