#!/usr/bin/env python

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

user_input = input("\nPlease enter a number to find largest prime factor: ")

def largest_prime_factor(n):

	#initialize variable to hold largest prime factor
	largest_factor = 1

	#remove any factors of 2
	test_factor = 2
	while n % test_factor == 0:
		# largest factor is at least 2
		largest_factor = test_factor
		# remove factor
		n = n / test_factor

	#remove any odd factors
	test_factor = 3
	#stop when we remove all factors
	while n != 1:
		# remove the factor as many times as it appears
		while n % test_factor == 0:
			# update largest_factor
			largest_factor = test_factor
			# remove factor
			n = n / test_factor
			#check next odd factor
		test_factor += 2
	return largest_factor

print largest_prime_factor(user_input)