pandigital_max = 987654321

'''def pandigital_list:
	pan_list = []
	for digit_9 in range(9,0,-1):
		for digit_8 in range(8,0,-1):
			for digit_7 in range(7, 0, -1):
				for digit_6 in range(6,0,-1):
					for digit_5 in range(5,0,-1):
						for digit_4 in range(4,0,-1):
							for digit_3 in range(3,0,-1):
								for digit_2 in range(2,0,-1)
									pan_item = str(digit_9) + str(digit_8) + str(digit_6)

'''

def pandigital_list():
	pan_list = []
	for digit_9 in range(9,0,-1):
		
		for digit_8 in range(9,0,-1):
			if digit_8 != digit_9:
				
				for digit_7 in range(9,0,-1):
					if (digit_7 != digit_9) and (digit_7 != digit_8):
					
						for digit_6 in range(9,0,-1):
							if (digit_6 != digit_7) and (digit_6 != digit_8) and (digit_6 != digit_9):

								for digit_5 in range(9,0,-1):
									if (digit_5 != digit_6) and (digit_5 != digit_7) and (digit_5 != digit_8) and (digit_5 != digit_9):

										for digit_4 in range(9,0,-1):
											if (digit_4 != digit_5) and (digit_4 != digit_6) and (digit_4 != digit_7) and (digit_4 != digit_8) and (digit_4 != digit_9):

												for digit_3 in range(9,0,-1):
													if (digit_3 != digit_4) and (digit_3 != digit_5) and (digit_3 != digit_6) and (digit_3 != digit_7) and (digit_3 != digit_8) and (digit_3 != digit_9):

														for digit_2 in range(9,0,-1):
															if (digit_2 != digit_3) and (digit_2 != digit_4) and (digit_2 != digit_5) and (digit_2 != digit_6) and (digit_2 != digit_7) and (digit_2 != digit_8) and (digit_2 != digit_9):
															
																for digit_1 in range(9,0,-1):
																	if (digit_1 != digit_2) and (digit_1 != digit_3) and (digit_1 != digit_4) and (digit_1 != digit_5) and (digit_1 != digit_6) and (digit_1 != digit_7) and (digit_1 != digit_8) and (digit_1 != digit_9):
																		
																		pan_item = str(digit_9) + str(digit_8) + str(digit_7) + str(digit_6) + str(digit_5) + str(digit_4) + str(digit_3) + str(digit_2) + str(digit_1)
																		pan_list.append(pan_item)
		return pan_list


def is_prime(n):
	# max factor to check is n/2
	max_divisor = n / 2
	
	# check evenness
	divisor = 2
	if (n % divisor == 0) and (n != 2):
		return False
	else:
		# check odd factors until you get to max
		divisor = 3
		while divisor <= max_divisor:
			if n % divisor == 0:
				return False
			divisor += 2
	return True


for i in pandigital_list():
	if is_prime(int(i)):
		print i
		