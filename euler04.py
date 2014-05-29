#!/usr/bin/env python

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(n):
	digits = []
	while n > 0:
		remainder = n % 10
		digits.append(remainder)
		n = (n - remainder) / 10
	for i in range(0, len(digits)/2):
		if digits[i] != digits[len(digits)-i-1]:
			return False
	return True

three_digits = range(100,1000)
three_digits.reverse()
max_palindrome = 0
for i in three_digits:
	for j in three_digits:
		if is_palindrome(i*j):
			if i * j > max_palindrome:
				max_palindrome = i * j
print max_palindrome