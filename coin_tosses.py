import random

def coin_tosses():
	heads = 0
	tails = 0
	for x in range(0, 5001):
		random_num = random.randint(0, 1)
		if (random_num == 0):
			print "Attempt #" + str(x) + " : Throwing a coin... It's a head!"
			heads +=1
			print "Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
		else:
			print "Attempt #" + str(x) + " : Throwing a coin... It's a tail!"
			tails +=1
			print "Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
		#arr.append(random_num)
coin_tosses()