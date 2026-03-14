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
