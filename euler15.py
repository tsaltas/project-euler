"""
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.

Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

import operator

def populate_dict(col_lens_dict, sequence, answer):
	"""
	Takes dictionary of Collatz lengths and a Collatz sequence
	Fills in the dictionary with the Collatz lengths of all the subproblems in the sequence
	"""
	for subproblem_inx, start_value in enumerate(sequence):
		if start_value not in col_lens_dict:
			col_lens_dict[start_value] = answer - subproblem_inx
	return col_lens_dict

def collatz_lengths(n):
	"""
	Generates an dictionary to store values of collatz sequences starting with key
	Fills in dictionary with lengths of Collatz sequences starting with numbers from 1 to n
	"""
	# initialize dictionary to hold lengths of collatz sequences
	col_lens = {}

	for i in range(1,n+1):
		sequence = [i]
		col_len = 0

		while i != 1:
			if i in col_lens:
				col_len = col_lens[i] + len(sequence) - 1
				i = 1
			else:
				if i % 2 == 0:
					i = i/2
				else:
					i = 3 * i + 1
				sequence.append(i)
		col_lens = populate_dict(col_lens, sequence, max(col_len, len(sequence)))

	return col_lens

# run script
if __name__ == "__main__":
	col_len = collatz_lengths(1000000)
	#print col_len
	print max(col_len.iteritems(), key=operator.itemgetter(1))[0]