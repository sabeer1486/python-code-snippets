table_num = int(input('enter table number : '))

for i in range(1,11):
	# print(f'{i} X {table_num} = {i * table_num}')
	print('{0} X {1} = {2}'.format(i, table_num, i * table_num))