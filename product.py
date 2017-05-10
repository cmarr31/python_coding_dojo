class Product(object):
	def __init__(self, price, item_name, weight, brand, cost, status = "for sale"):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status

	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self, tax_num):
		self.price + tax_num
		return self

	def return_method(self, str):
		if (str == "defective"):
			self.price = 0
		elif (str == "new"):
			self.status = "for sale"
		elif (str == "open"):
			self.price *= 0.2
		else:
			print "I'm going to have to ask you to leave."
		return self

	def display_info(self):
		print self.price
		print self.item_name
		print self.weight
		print self.brand
		print self.cost
		print self.status
		return self