# program starts from main
def hcf(numbers):
	# assing smallest number
	small_num = numbers[0]

	# calculating factors for smallest number
	small_num_factors = [i for i in range(1, small_num+1) if small_num % i == 0] 

	# looping the factors in reverse order
	for factor in small_num_factors[::-1]:

		# lst gets empty for every new factor
		lst = []

		# this loop check the 'factor' is divisor for every 'num' value
		for num in numbers:
			if num % factor == 0:

				# append 1 if 'factor' is divisor of 'num'
				lst.append(1)            
				if len(lst) == len(numbers):

					# return factor vlaue if number of elemnts of 'lst' equal to number of elements in 'numbers'
					return factor

def lcm(numbers):
	# chose maximum number 
	max_num =numbers[len(numbers) - 1]
	while True:
		lst = []
		for num in numbers:
			# loop until the max_num is divided by all the number
			if max_num % num == 0:
				lst.append(1)
				if len(lst) == len(numbers):
					return max_num
			else:
				# increment max_num until it is divided by all the numbers
				max_num = max_num + 1

def main(): 
	while True:
		choice = int(input('Enter your choice \n 1: LCM \n 2: HCF \n'))
		if choice in [1,2]:
			break

	print('Enter list of numbers with space saperation: ', end='')
	# user input is splitted & sorted 
	num_list = sorted(list(map(int, input().split())))

	if choice == 1:
		print('LCM = ',lcm(num_list))
	else:
		print('HCF = ',hcf(num_list))

main()
	