import random
from beverages import HotBeverage


class CoffeeMachine:
	"""Una máquina de café que sirve bebidas calientes."""
	
	class EmptyCup(HotBeverage):
		"""Representa una taza vacía."""
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90
		
		def description(self):
			return "An empty cup?! Gimme my money back!"
	
	class BrokenMachineException(Exception):
		"""Excepción que se levanta cuando la máquina está rota."""
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
	
	def __init__(self):
		"""Constructor: inicializa la máquina en estado funcional."""
		self.drinks_served = 0
		self.is_broken = False
	
	def repair(self):
		"""Repara la máquina y la vuelve a poner en funcionamiento."""
		self.drinks_served = 0
		self.is_broken = False
	
	def serve(self, beverage_class):
		"""
		Sirve una bebida o una taza vacía aleatoriamente.
		
		Parameters:
			beverage_class: Una clase que hereda de HotBeverage
		
		Returns:
			Una instancia de beverage_class o una EmptyCup
		
		Raises:
			BrokenMachineException: Si la máquina está rota
		"""
		# Verificar si la máquina está rota
		if self.is_broken:
			raise CoffeeMachine.BrokenMachineException()
		
		# Incrementar contador de bebidas servidas
		self.drinks_served += 1
		
		# Verificar si la máquina se rompe después de esta bebida
		if self.drinks_served >= 10:
			self.is_broken = True
		
		# Retornar aleatoriamente la bebida o una taza vacía
		if random.choice([True, False]):
			return beverage_class()
		else:
			return CoffeeMachine.EmptyCup()


# Tests
if __name__ == "__main__":
	from beverages import Coffee, Tea, Chocolate, Cappuccino
	
	machine = CoffeeMachine()
	
	# Servir bebidas hasta que se rompa
	beverages_to_try = [Coffee, Tea, Chocolate, Cappuccino]
	
	print("=" * 50)
	print("PRIMERA RONDA - Sirviendo bebidas")
	print("=" * 50)
	
	try:
		for i in range(12):  # Intentar servir más de 10
			beverage_class = random.choice(beverages_to_try)
			drink = machine.serve(beverage_class)
			print(f"Bebida #{i+1}: {drink.name} - ${drink.price:.2f}")
	
	except CoffeeMachine.BrokenMachineException as e:
		print(f"\n❌ {e}")
		print("La máquina se rompió después de servir 10 bebidas")
	
	# Reparar la máquina
	print("\n" + "=" * 50)
	print("Reparando la máquina...")
	print("=" * 50)
	machine.repair()
	
	# Servir de nuevo
	print("\nSEGUNDA RONDA - Sirviendo bebidas después de la reparación")
	print("=" * 50)
	
	try:
		for i in range(12):  # Intentar servir más de 10 nuevamente
			beverage_class = random.choice(beverages_to_try)
			drink = machine.serve(beverage_class)
			print(f"Bebida #{i+1}: {drink.name} - ${drink.price:.2f}")
	
	except CoffeeMachine.BrokenMachineException as e:
		print(f"\n❌ {e}")
		print("La máquina se rompió de nuevo después de servir 10 bebidas")
