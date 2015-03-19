"""
Square digit chains
"""

def digit_chains(n):
	""" returns number of starting nos below n terminating in 89 """
	
	# Create a dict where dict[n] is the sum of all digits in n
	sum_digits_squared = {}

	final_arr = {}
	num_filled = 0
	curr = 1

	while num_filled < n - 1:
		#print "current is " + str(curr)
		# if current num already in table, go to next number
		if curr in final_arr:
			curr +=1
		else:
			# else, create the digit chain
			done = False
			while done == False:
				digit_chain = [curr]
				curr_digit = curr
				indicator = None
				while (curr_digit != 1 and curr_digit != 89):
					#print "curr digit: " + str(curr_digit)
					curr_sum = 0
					curr_string = str(curr_digit)
					for char in curr_string:
						curr_sum += int(char)**2
					curr_digit = curr_sum
					if curr_digit in final_arr:
						indicator = final_arr[curr_digit]
						done = True
					digit_chain.append(curr_digit)
				if curr_digit == 1:
					#print "setting indicator to 0"
					indicator = 0
				elif curr_digit == 89:
					indicator = 1
				else:
					print "ERROR OCCURRED"
				done = True
			# once digit chain terminates, label all digits in digit chain not in array
			for digit in digit_chain:
				#print "adding to dictionary: " + str(digit)
				if digit not in final_arr:
					final_arr[digit] = indicator
			num_filled += 1
			curr += 1
	final_arr = dict((key,value) for key, value in final_arr.iteritems() if key <n)
	#print final_arr
	return sum(final_arr.values())

def euler92(limit):
    # Let sumsq uphold the invariant that the nth element contains
    # the sum of the squares of the digits of n, or better yet, a
    # value somewhere along its reduction chain.

    # Start with the base case: chain[0] = sum(0 * 0) = 0.
    # Also preallocate many unknowns...
    sumsq = [sum((0 * 0,))] + [None] * max(limit, 162)

    # ... and fill them in.  Note how we reuse previous sums!
    for i in xrange(max(1 + limit, 163)):
        sumsq[i] = (i % 10) ** 2 + sumsq[i // 10]

    # Keep reducing each element until everything has converged
    # on either 1 or 89.
    all_converged = False
    while not all_converged:
        all_converged, eighty_nines = True, 0
        for i in xrange(1, 1 + limit):
            if sumsq[i] == 1:
                pass
            elif sumsq[i] == 89:
                eighty_nines += 1
            else:
                all_converged = False
                # sumsq[sumsq[i]] is a quick way to calculate
                # the sum of the squares of the digits, and maybe
                # even skip a few steps down the chain.
                sumsq[i] = sumsq[sumsq[i]]
    return eighty_nines

if __name__ == "__main__":
	#print digit_chains(10000)
	print euler92(10000000)