"""
Special Pythagorean triplet
"""

def find_triple_sum(sum_total):
	diagonal_sum = 2
	#print 'diagonal_sum is {0}'.format(diagonal_sum)
	while 1:
		for i in range(1,diagonal_sum):
			#print 'i is {0}'.format(i)
			j = diagonal_sum - i
			k = j + 1
			#print 'j is {0}'.format(j)
			#print 'k is {0}'.format(k)
			while i*i + j*j > k*k:
				k += 1
				#print 'k is {0}'.format(k)
			if i*i + j*j == k*k:
				#print 'found triplet {0}, {1}, {2}'.format(i,j,k)
				if i + j + k == sum_total:
					#print 'sum to 1000'
					return [i,j,k]
		diagonal_sum += 1

triple_list = find_triple_sum(1000)
print triple_list
print 'product is {0}'.format(triple_list[0] * triple_list[1] * triple_list[2])