import sys
file = open(sys.argv[1], 'r')

triangle_array = []

for line in file:
	line = line.split()
	line = [int(i) for i in line]
	triangle_array.append(line)

#print triangle_array
#print triangle_array[len(triangle_array)-1]

for i in range(len(triangle_array) - 1, 0, -1):
	lower_row = triangle_array[i]
	for j in range(0, len(triangle_array[i-1])):
		left = lower_row[j]
		right = lower_row[j+1]
		triangle_array[i-1][j] += max(left, right)

print triangle_array[0]