"""
In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
"""

import sys
file = open(sys.argv[1], 'r')

# 20X20 grid
n = 20
# product of 4 numbers
k = 4

# initialize max product
max_product = 0

# create matrix to represent the grid
grid = []
for line in file:
	line = line.split()
	line = [int(i) for i in line]
	grid.append(line)

#print grid
#print grid[0]

# up/down products
# go through all columns
for col in range(0, n):
	# look down the rows in given column, want to get to row 16 to multiply 16*17*18*19
	for row in range(0, n - k + 1):
		product = 1
		for i in range(0,k):
			product *= grid[row+i][col]
		if product > max_product: max_product = product

# left/right products
# go through all rows
for row in range(0, n):
	# look across the columns in given row, want to get to column 16 to multiply 16*17*18*19
	for col in range(0, n - k + 1):
		product = 1
		for i in range(0,k):
			product *= grid[row][col+i]
		if product > max_product: max_product = product

# diagonals that go down from left to right
# go through all the rows, need to get to row 16
for row in range(0, n - k + 1):
	# look across the columns in given row, need to get to column 16
	for col in range(0, n - k + 1):
		product = 1
		for i in range(0,k):
			product *= grid[row+i][col+i]
		if product > max_product: max_product = product

# diagonals that go up from left to right
# go through all the rows, start at bottom and work way up to 3
for row in [item for item in reversed(range(3, 20))]:
	# look across the columns in given row, need to get to column 16
	for col in range(0, n - k + 1):
		product = 1
		for i in range(0,k):
			product *= grid[row-i][col+i]
		if product > max_product: max_product = product

print max_product