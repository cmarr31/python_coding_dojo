def odd_even():
	for x in range(1, 2001):
		iteration = "Number is " + str(x) + ". "
		if (x % 2 == 0):
			even_num = iteration + "This is an even number."
			print even_num
		else:
			odd_num = iteration + "This is an odd number."
			print odd_num
odd_even()


def multiply(lst, num):
	new_lst = []
	for x in lst:
		new_lst.append(x * num)
	print new_lst
	return new_lst
		

multiply([2,10,20], 5)