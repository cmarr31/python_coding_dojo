class Bike(object):

	def __init__(self, price, max_speed, miles = 0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print self.price
		print self.max_speed
		print self.miles
		return self

	def ride(self):
		print "Riding"
		self.miles += 10
		print self.miles
		return self


	def reverse(self):
		print "Reversing"
		if (self.miles >= 5):	
			self.miles -= 5
		else:
			print "You haven't gone anywhere yet."
		print self.miles
		return self



bike1 = Bike(200, 20)
bike2 = Bike(201, 21)
bike3 = Bike(202, 22)

bike1.displayInfo().ride().reverse()


bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()









