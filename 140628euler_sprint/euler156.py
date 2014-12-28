def generate_fib(n):
	"""Generates the Fibonacci numbers <= n"""
	fib_list = [1,2]
	fib_1 = 1
	fib_2 = 2
	while max(fib_list) < n:
		new_fib = fib_1 + fib_2
		fib_list.append(new_fib)
		fib_1 = fib_2
		fib_2 = new_fib
	return fib_list

#print generate_fib(100)

def zeck_rep(n):
	"""returns the Zeckendorf representation of a positive integer n"""
	fib_list = generate_fib(n)
	# find the terms that sum to n