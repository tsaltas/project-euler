"""
Lattice paths
"""

def	factorial(n):
	if n == 0:
		return None
	elif n == 1:
		return 1
	else:
		prod = 1
		for i in range(2, n+1):
			prod *= i

		return prod

def lattice_paths(n):
	"""
	Find the number of paths through a lattice of size nXn
	"""
	return factorial(2*n) / (factorial(n) * factorial(n))
	
if __name__ == "__main__":
	print lattice_paths(2)
	print lattice_paths(3)
	print lattice_paths(20)