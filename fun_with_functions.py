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


def layered_multiples(arr):
	new_arr = []
	b = len(arr)
	counter = 0
	list_num = 0
	for y in arr:
		counter = 0
		new_arr.append([])
		while (counter < y):
			new_arr[list_num].append(1)
			counter +=1
		list_num +=1
	return new_arr
x = layered_multiples(multiply([2,4,5],3))
print x