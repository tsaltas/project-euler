#!/usr/bin/env python

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

n_to_factor = input("\nPlease enter a number to find largest prime factor: ")

'''
def find_factor(n):
	for i in range(2,n+1):
		if n % i == 0:
			return i
		else: i += 1
'''

def is_prime(n):
	if n == 1: return False
	for i in range(2, n/2+1):
		if n % i == 0: return False
	return True

# if n is prime, largest prime factor is n
if is_prime(n_to_factor):
	print n_to_factor
# else construct prime_list using sieve of eratosthenes and test primes up to n / 2
else:
	# initialize list of numbers up to n / 2
	prime_list = range(2,n_to_factor/2 + 1)
	# initialize the index to work through the sieve
	prime_list_index = 0
	prime_list_length = len(prime_list)
	
	# remove multiples of each prime without over-indexing
	while prime_list_index < prime_list_length:
		current_prime = prime_list[prime_list_index]
		#print 'prime list index is ' + str(prime_list_index)
		#print 'current prime is ' + str(current_prime)
		# from the list, starting after the current prime we are working on
		i = prime_list_index + 1
		while i < prime_list_length:
			#print 'i is ' + str(i)
			# if an element in the list is a multiple of the current prime
			#print 'testing primality of ' + str(prime_list[i])
			if prime_list[i] % current_prime == 0:
				#print 'it''s not prime'
				# then remove it from the list
				prime_list.remove(prime_list[i])
				prime_list_length -= 1
			# test the next item in the list
			i+= 1
		# go to next prime in list to remove multiples
		prime_list_index += 1

	# reverse the list of primes so we test in descending order
	prime_list.reverse()

	# test to find the largest prime that is a factor
	for i in range(0, len(prime_list)):
		if n_to_factor % prime_list[i] == 0:
			print prime_list[i]


'''
# Create tree data structure for the prime factorization tree
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

# Create a factor tree for n_to_factor and keep factoring until we get the prime factorization

# find any initial factorization for n_to_factor. factor_1 should be < factor_2
factor_1 = find_factor(n_to_factor)
factor_2 = n / factor_1


# initialize the tree
root = Tree()
root.data = n_to_factor
root.left = Tree()
root.left.data = factor_1
root.right = Tree()
root.right.data = factor_2

while !is_prime(factor_1):
	

# Return the largest prime factor from the factor tree

'''