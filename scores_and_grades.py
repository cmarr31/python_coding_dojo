import random

def scores_and_grades():
	arr = []
	for x in range(0, 10):
		random_num = random.randint(60, 100)
		arr.append(random_num)
	for x in arr:
		y = str(x)
		print "Scores and Grades"
		if (x < 60):
			print "Score: " + y + "; Your grade is F"
		elif (x < 70):
			print "Score: " + y + "; Your grade is D"
		elif (x < 80):
			print "Score: " + y + "; Your grade is C"	
		elif (x < 90):
			print "Score: " + y + "; Your grade is B"
		else:
			print "Score: " + y + "; Your grade is A"
	print "End of the program. Bye!"

scores_and_grades()