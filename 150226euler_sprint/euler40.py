def multiples_func(n):
	"""
	Find sum of all multiples of 3 or 5 below 1000
	"""
	num_list = range(1,n)
	num_list = filter(lambda x: ((x % 3 == 0) or (x % 5 == 0)), num_list)
	return reduce(lambda x,y:x+y, num_list)

if __name__ == "__main__":
	print multiples_func(1000)