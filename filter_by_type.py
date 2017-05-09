def filter_by_type(x):
	dt = type(x)
	if (isinstance(x, int) == True):
		if (x >= 100):
			print "That's a big number!"
		else:
			print "That's a small number."
	elif (isinstance(x, str) == True):
		if (len(x) >= 50):
			print "Long sentence."
		else:
			print "Short sentence."
	elif (isinstance(x, list) == True):
		if (len(x) >= 10):
			print "Big list!"
		else:
			print "Short list."
	else:
		return "idk bruh."

filter_by_type([1, 6, 31])