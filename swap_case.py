def swap_case(s):
	lst = []
	for i in s:
		if i.isupper():
			lst.append(i.lower())
		else:
			lst.append(i.upper())
	s = ''.join(lst)
	return s

result = swap_case(str(input("Enter your sting for swap case: ")))
print(result)