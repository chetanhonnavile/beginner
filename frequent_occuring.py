#!/usr/bin/python


from collections import Counter

class Frequent():


	def __init__(self,list1):
		self.list1 = list1
		if  len(list1) > 1:
			dic = Counter(list1)
			for key,value in dic.items():
				if max(dic.values()) == value:
					print key,"is the most frequent occuring element for",value,"times"
		else:
			print "Input list containing more than one element"


def most_frequent(given_list):
    if len(given_list) <= 1 and len(given_list) == 0:
        return None
    else:
        for key,value in Counter(given_list).items():
            if max(Counter(given_list).values()) == value:
                return key


freq = Frequent(['a','v','r','p','p','c','v','v','r','r','r'])
