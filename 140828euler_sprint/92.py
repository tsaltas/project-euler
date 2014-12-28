from math import *

def square_digits(n):
	string_n = str(n)
	string_n = list(string_n)
	squares = map(lambda x: int(x)*int(x), string_n)
	return reduce(lambda x, y: x+y, squares)

#print square_digits(58)

def find_parents(number, digits):
	max_square = floor(sqrt(number))
	max_addends = [7, 6, 7, 7, 5, 3, 2, 1, 1, 1]
	
