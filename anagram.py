#!/usr/bin/python


def anagram(str1,str2):
	if sorted(list(str1)) != sorted(list(str2)):
		return "yes,anagram"
	else:
		return "No anagram"
		
		
print anagram('clip','plisc')
