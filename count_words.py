#count number of words in a sentence


#!/usr/bin/python


def cou(stri):
	return stri.count(" ")+1

def cou1(stri):
	return len(stri.split())


print cou("this is my mac!!")
print cou1("this is my mac from split")
