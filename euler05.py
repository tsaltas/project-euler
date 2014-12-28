"""
  2520 is the smallest number that can be divided by each of the numbers
   from 1 to 10 without any remainder.

   What is the smallest number that is evenly divisible by all of the numbers
   from 1 to 20?
"""

def prime_factorization(n):
	#initialize set to hold prime factors
	prime_factors = []

	#remove any factors of 2
	test_factor = 2
	while n % test_factor == 0:
		# there was another factor of 2
		prime_factors.append(test_factor)
		# remove factor
		n = n / test_factor

	#count odd factors
	test_factor = 3
	#stop when we remove all factors
	while n != 1:
		# remove the factor as many times as it appears
		while n % test_factor == 0:
			# stick it in the prime factor list
			prime_factors.append(test_factor)
			# remove factor
			n = n / test_factor
			#check next odd factor
		test_factor += 2
	return prime_factors


def smallest_number(n):
	factor_list = [1]
	for i in range(2,n+1):
		prime_factors = prime_factorization(i)
		for j in prime_factors:
			while prime_factors.count(j) > factor_list.count(j):
				factor_list.append(j)
	return reduce(lambda x, y: x * y, factor_list)

print smallest_number(20)
	