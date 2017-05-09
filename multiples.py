def print_odds():
	i = 0
	while (i < 1000):
		i +=1
		print i

print_odds()

def print_mults_five():
	for x in range(5,1000005):
		if (x % 5 == 0):
			print x

print_mults_five()

a = [1, 2, 5, 10, 255, 3]

def sum_list(arr):
	x = 0
	while (x < len(arr)):
		print arr[x]
		x +=1

sum_list(a)

def average_list(arr):
	avg = sum(arr)/len(arr)
	print avg

average_list(a)