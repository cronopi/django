import random
from beverages import HotBeverage


class CoffeeMachine:
	def __init__(self):
		self.drinks = 0
		self.is_broken = False

	class Emptycup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.drinks = 0
		self.is_broken = False

	def serve(self, beverage):
		if self.is_broken:
			raise self.BrokenMachineException()
		self.drinks += 1
		if self.drinks >= 10:
			self.is_broken = True
		if random.choice([True, False]):
			return beverage()
		else:
			return self.Emptycup()
