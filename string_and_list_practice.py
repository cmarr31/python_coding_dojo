## 1) Find and replace:
# In this string: str = "It's thanksgiving day. It's my birthday,too!" print the position of the 
# first instance of the word "day". Then create a new string where the word "day" is 
# replaced with the word "month".

def find_and_replace(str):
	position = str.find("day")
	print position
	second_str = str.replace("day", "month", 1)
	print second_str

find_and_replace("It's thanksgiving day. It's my birthday,too!")

def min_and_max(lst):
	print min(lst)
	print max(lst)

z = [1, 5, 34, 8, -3, 3, 6, 55]

min_and_max(z)


def first_and_last(lst):
	print lst[0]
	print lst[-1]
	lst.sort()
	print lst

first_and_last(z)

import math

def new_list(lst):
	lst.sort()
	half_way_point = len(lst)
	half_way_point /=2

	floor_num = math.floor(half_way_point)
	array = []

	for i in range(0, int(floor_num)):
		array.append(i)
	lst.insert(0, array)
	
	print lst

new_list(z)


































