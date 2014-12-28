import itertools

def generate_sets():
	""" Generates all sets (a,b,c,d) of digits 0-9 such that a < b < c < d """
	return list(itertools.combinations(range(1, 10), 4))

def generate_expressions(digits_set):
	""" Given one set of digits a < b < c < d, generate all expressions by permuting those digits and adding in operators """
	operators = ["+","-","/","*"]
	# find all permutations of operators
	operator_perms = [item for item in itertools.product(operators,repeat=3)]
	# find all permutations of the digits in the set
	digit_perms = [item for item in itertools.permutations(digits_set)]

	# find all combinations of digits and operators and put into list of expressions
	expression_list = []
	for digits in digit_perms:
		for ops in operator_perms:
			expression_list.append(digits[0] + ops[0] + digits[1] + ops[1] + digits[2] + ops[2] + digits[3])

	return expression_list

def parenthesize_expression(expr):
	""" Given an expression with digits and operators, parenthesize in all possible ways and evaluate"""
	parens_list = []
	
	# base case: expression has length 3 like "a+b"
	if len(expr) == 7:
		return [expr, "(" + expr + ")"]
	# otherwise, try dividing based on all possible pivots
	else:
		for left_side in parenthesize_expression(expr[:len(expr) - 4]):
			parens_list.append(left_side + expr[len(expr)-4:])
			parens_list.append("(" + left_side + expr[len(expr)-4:]+ ")")
		for right_side in parenthesize_expression(expr[4:]):
			parens_list.append(expr[:4] + right_side)
			parens_list.append("(" + expr[:4] + right_side + ")")

	return [item for item in set(parens_list)]

def generate_integers(digits):
	expressions = generate_expressions(digits)
	#print "expressions "
	#print expressions
	parenthesized = []
	for expr in expressions:
		parenthesized += parenthesize_expression(expr)
	#print "parenthesized "
	#print parenthesized
	ints_generated = []
	for paren in parenthesized:
		try:
			ints_generated.append(eval(paren))
		except ZeroDivisionError:
			pass
	ints_generated = [int(item) for item in set(ints_generated) if (round(item) == item and item > 0)]
	ints_generated.sort()
	return ints_generated

def max_sequence(array):
	""" Takes an array of sorted ints, figures out the max consecutive sequence length """
	max_length = 0
	current_length = 1
	for i in range(1, len(array)):
		if array[i] == array[i-1] + 1:
			current_length += 1
		else:
			current_length = 1
		if current_length > max_length:
			max_length = current_length

	return max_length

def find_max_integer_set():
	digit_set = generate_sets()
	sequence_dict = {}
	for digit in digit_set:
		sequence_dict[digit] = max_sequence(generate_integers(digit))

	return max(sequence_dict.values())