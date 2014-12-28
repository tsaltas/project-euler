sum = 0
max = 10**10

for i in range(1,1001):
	sum += i**i
	sum = sum % max

print sum