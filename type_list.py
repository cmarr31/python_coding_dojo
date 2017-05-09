def type_list(lst):
	new_str = ""
	new_sum = 0
	
	for x in lst:
		if (isinstance(x, int) == True):
			new_sum += x
		elif (isinstance(x, str) == True):
			new_str += x

	print new_str
	print new_sum

x = ["joe", 31, "whaaa", 202, "lol"]

type_list(x)