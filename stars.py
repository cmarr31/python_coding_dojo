def draw_stars(lst):
	new_arr = []
	b = len(lst)
	counter = 0
	list_num = 0
	for y in lst:
		counter = 0
		new_arr.append([])
		while (counter < y):
			new_arr[list_num].append("*")
			counter +=1
		list_num +=1
	print new_arr	
	return new_arr
draw_stars([4, 6, 1, 3, 5, 7, 25])
