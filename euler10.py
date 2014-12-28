"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def generate_array(n):
	""" generates list of size n + 1 initialized to TRUE """
	return [True] * (n+1)

def sieve_of_eratosthenes(prime_list):
	""" Takes an list of size n initialized to TRUE and sets non-prime indices equal to false (e.g. array[2] = True, array[4] = False)"""
	# 0 and 1 are neither prime nor composite
	prime_list[0] = "N/A"
	prime_list[1] = "N/A"

	for i in range(2,len(prime_list)-1):
		if (prime_list[i] == True):
			multiple = 2*i
			while (multiple < len(prime_list)):
				prime_list[multiple] = False
				multiple += i
	return [item[0] for item in enumerate(prime_list) if item[1]]

# run script
if __name__ == "__main__":
	print reduce(lambda x,y: x + y, sieve_of_eratosthenes(generate_array(2000000)))-1