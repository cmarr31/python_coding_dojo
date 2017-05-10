class Car(object):

	def __init__(self, price, speed, fuel, mileage, tax = 0.12):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = tax
		if (self.price > 10000):
			self.tax = 0.15
		self.display_all()

	def display_all(self):
		print self.price
		print self.speed
		print self.fuel
		print self.mileage
		print "Tax: " + str(self.tax)
		return self

mustang = Car("Price: 5000", "Speed: 160", "Fuel: Empty", "Mileage: 25mpg")