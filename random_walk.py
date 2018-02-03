#!/usr/bin/python

import random

def random_walk(n):
	x=0 
	y = 0
	for i in range(n):
		dir = random.choice(["n","e","w","s"])
		if dir == "n":
			y+=1
		elif dir == "e":
			x+=1
		elif dir == "w":
			x-=1
	    	else:
			y-=1
	return (x,y),"{0} blocks away from origin".format(abs(x)+abs(y))
	
print random_walk(20)
