def champ_const(n):
	constant = "0."
	for i in range(1,n):
		constant += str(i)
	return constant

answer = champ_const(1000000)
#print answer
#print 'length is ' + str(len(answer))

d_1 = int(answer[1 + 1])
d_10 = int(answer[1 + 10])
d_100 = int(answer[1 + 100])
d_1000 =  int(answer[1 + 1000])
d_10000 =  int(answer[1 + 10000])
d_100000 =  int(answer[1 + 100000])
d_1000000 =  int(answer[1 + 1000000])

print d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000