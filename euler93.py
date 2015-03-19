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
			expression_list.append(str(digits[0]*1.0) + ops[0] + str(digits[1]*1.0) + ops[1] + str(digits[2]*1.0) + ops[2] + str(digits[3]*1.0))

	return expression_list

def parenthesize_expression(expression):
	""" Given an expression with digits and operators, parenthesize in all possible ways and evaluate"""
	return [
        # no parens
        expression,
        # (a+b)+c+d
        "(" + expression[0:7] + ")" + expression[7:],
        # a+(b+c)+d
        expression[0:4] + "(" + expression[4:11] + ")" + expression[11:],
        # a+b+(c+d)
        expression[0:8] + "(" + expression[8:] + ")",
        # (a+b) + (c+d)
        "(" + expression[0:7] + ")" + expression[7:8] + "(" + expression[8:] + ")",
        # ((a+b)+c) + d
        "((" + expression[0:7] + ")" + expression[7:11] + ")" + expression[11:],
        # (a + (b + c)) + d
        "(" + expression[0:4] + "(" + expression[4:11] + "))" + expression[11:],
        # a + (b + (c+d))
        expression[0:4] + "(" + expression[4:8] + "(" + expression[8:] + "))",
        # a + ((b + c ) + d)
        expression[0:4] + "((" + expression[4:11] + ")" + expression[11:] + ")"
    ]

def generate_integers(digits):
	expressions = generate_expressions(digits)
	parenthesized = []
	for expr in expressions:
		parenthesized += parenthesize_expression(expr)
	ints_generated = []
	value_dict = {}
	for paren in parenthesized:
		try:
			value = eval(paren)
			if (value > 0 and round(value) == value):
				value_dict[value] = paren
			ints_generated.append(value)
		except ZeroDivisionError:
			pass
	ints_generated = [int(item) for item in set(ints_generated) if (round(item) == item and item > 0)]
	ints_generated.sort()
	#return ints_generated
	return value_dict
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

	max_run_len = max(sequence_dict.values())

	for item in sequence_dict.iteritems():
		if item[1] == max_run_len:
			max_digit = item[0]

	return (max_digit, max_run_len)

# Run Script
if __name__ == "__main__":
    #print generate_expressions((1,2,3,4))
    #print generate_integers(("1.0","2.0","3.0","4.0"))
    print generate_integers((1,2,5,8))
    #print find_max_integer_set()