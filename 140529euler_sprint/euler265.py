binary_numbers = []
binary_numbers.append('00000')

def build_binary_lists(n):
	binary_lists = []
	initial_element = ''
	tree_depth = 0
	for i in range(0,n):
		initial_element += '0'

	left = initial_element[1:] + '0'
	right = initial_element[1:] + '1'
	print left
	print right

	if set(initial_element) != set(initial_element).union(left):
		


build_binary_lists(5)



