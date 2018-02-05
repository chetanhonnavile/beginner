#!/usr/bin/python

from collections import OrderedDict

a = ['1','2',3,'4','2','1',5,6,9]
a = list(OrderedDict.fromkeys(a))
print a  
