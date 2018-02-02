#!/usr/bin/python

#construct a truth table

def foo(n):
	truth_table = [ (i,not i%3,not i%5) for i in range(1,n)]
	message = {(True,True):"FizzBuzz",(True,False):"Fizz",(False,True):"Buzz",(False,False):""}
	results = [ message[(j,k)] or i for (i,j,k) in truth_table]
	for result in results:
		print result
		
		
		
		
foo(20)
