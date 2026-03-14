

class HotBeverage:
	def __init__(self):
		self.name = "hot beverage"
		self.price = 0.30

	def __description__(self):
		return "Just some hot water in a cup."

	def __str__(self):
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.__description__()}"



beverage = HotBeverage()

# Opción 1: Con print()
print(beverage)
