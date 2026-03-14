import random
from beverages import HotBeverage


class CoffeeMachine:
	def __init__(self):
		self.drinks = 0
		self.is_broken = False
