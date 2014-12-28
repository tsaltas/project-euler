"""
  The sum of the squares of the first ten natural numbers is,
                          1^2 + 2^2 + ... + 10^2 = 385

   The square of the sum of the first ten natural numbers is,
                       (1 + 2 + ... + 10)^2 = 55^2 = 3025

   Hence the difference between the sum of the squares of the first ten
   natural numbers and the square of the sum is 3025 385 = 2640.

   Find the difference between the sum of the squares of the first one
   hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n):
	sum_squares = 0
	for i in range(1, n+1):
		square = i * i
		sum_squares += square
	return sum_squares

def square_of_sums(n):
	sum_of_nums = 0
	for i in range(1, n+1):
		sum_of_nums+= i
	return sum_of_nums * sum_of_nums

print square_of_sums(100) - sum_of_squares(100)