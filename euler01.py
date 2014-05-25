#!/usr/bin/env python

'''
Project Euler problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''
input_max = input("\nPlease enter maximum natural number: ")

sum = 0

for x in range (1, input_max):
	if (x / 3) * 3 == x:
		sum = sum + x
	elif (x / 5) * 5 == x:
		sum = sum + x

print "\n" + str(sum) + " is the sum of integers from 1 to " + str(input_max) + " divisible by either 3 or 5.\n"
		