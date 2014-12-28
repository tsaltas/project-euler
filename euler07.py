"""
  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
   that the 6^th prime is 13.

   What is the 10001^st prime number?
"""

def prime(n):
	prime_index = 2
	prime_list = [2,3]
	current_number = 3
	while prime_index < n:
		current_number += 2
		if prime_test(current_number):
			prime_list.append(current_number)
			prime_index += 1
	return prime_list

def prime_test(n):
	if n < 2:
		return -1
	if n == 2:
		return True
	if n == 3:
		return True
	else:
		for i in range(2,n/2):
			if (n % i == 0):
				return False
		return True;

# Run Script
if __name__ == "__main__":
    print prime(10001)[10000]