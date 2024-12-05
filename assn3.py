# Patrick Miller
# Assignment 3

from abc import ABC, abstractmethod
import inquirer

class Pizza(ABC):
	@abstractmethod
	def get_description(self):
		pass

	@abstractmethod
	def get_cost(self):
		pass

class MargheritaPizza(Pizza):
	def get_description(self):
		return "Margherita Pizza"

	def get_cost(self):
		return 15.0

class PepperoniPizza(Pizza):
	def get_description(self):
		return "Pepperoni Pizza"

	def get_cost(self):
		return 18.0

class VeggiesPizza(Pizza):
	def get_description(self):
		return "Veggie Pizza"

	def get_cost(self):
		return 16.0

class Sauce(Pizza):
	# Decorator
	# Each sauce is a decorator that wraps a pizza object, which in the CLI is the Pizza
	# each Sauce implementation is responsible for appending the sauce and adding the cost
	def __init__(self, pizza):
		self.pizza = pizza
		super().__init__()

class TomatoSauce(Sauce):
	def __init__(self, pizza):
		super().__init__(pizza)

	def get_description(self):
		return self.pizza.get_description() + " with Tomato Sauce"

	def get_cost(self):
		return self.pizza.get_cost() + 0.5

class BarbecueSauce(Sauce):
	def __init__(self, pizza):
		super().__init__(pizza)

	def get_description(self):
		return self.pizza.get_description() + " with Barbecue Sauce"

	def get_cost(self):
		return self.pizza.get_cost() + 1.0

class PestoSauce(Sauce):
	def __init__(self, pizza):
		super().__init__(pizza)

	def get_description(self):
		return self.pizza.get_description() + " with Pesto Sauce"

	def get_cost(self):
		return self.pizza.get_cost() + 1.5

class Topping(Pizza):
	# Decorator
	# Each topping is a decorator that wraps a pizza object, which in the CLI is the Sauce object
	# each Topping implementation is responsible for appending the topping and adding the cost
	def __init__(self, pizza):
		self.pizza = pizza
		super().__init__()

class CheeseTopping(Topping):
	def __init__(self, pizza):
		super().__init__(pizza)

	def get_description(self):
		return self.pizza.get_description() + ", Cheese"

	def get_cost(self):
		return self.pizza.get_cost() + 1.0

class OliveTopping(Topping):
	def __init__(self, pizza):
		super().__init__(pizza)

	def get_description(self):
		return self.pizza.get_description() + ", Olive"

	def get_cost(self):
		return self.pizza.get_cost() + 0.5

class MushroomTopping(Topping):
	def __init__(self, pizza):
		super().__init__(pizza)

	def get_description(self):
		return self.pizza.get_description() + ", Mushroom"

	def get_cost(self):
		return self.pizza.get_cost() + 0.5

class PepperToping(Topping):
	def __init__(self, pizza):
		super().__init__(pizza)

	def get_description(self):
		return self.pizza.get_description() + ", Pepper"

	def get_cost(self):
		return self.pizza.get_cost() + 0.5

def cli():
	print("                 Create a Pizza")
	print("=================================================")
	print("Space selects, Enter toggles, and Arrows navigate")
	print("=================================================")
	questions = [
		inquirer.List('pizza',
			message="What pizza would you like?",
			choices=['Margherita', 'Pepperoni', 'Veggie'],
		),
		inquirer.List('sauce',
			message="What sauce would you like?",
			choices=['Tomato', 'Barbecue', 'Pesto'],
		),
		inquirer.Checkbox('topping',
			message="What toppings would you like?",
			choices=['Cheese', 'Olive', 'Mushroom', 'Pepper'],
		),
	]

	answers = inquirer.prompt(questions)

	if answers['pizza'] == 'Margherita':
		pizza = MargheritaPizza()
	elif answers['pizza'] == 'Pepperoni':
		pizza = PepperoniPizza()
	elif answers['pizza'] == 'Veggie':
		pizza = VeggiesPizza()

	if answers['sauce'] == 'Tomato':
		pizza = TomatoSauce(pizza)
	elif answers['sauce'] == 'Barbecue':
		pizza = BarbecueSauce(pizza)
	elif answers['sauce'] == 'Pesto':
		pizza = PestoSauce(pizza)

	for topping in answers['topping']:
		if topping == 'Cheese':
			pizza = CheeseTopping(pizza)
		elif topping == 'Olive':
			pizza = OliveTopping(pizza)
		elif topping == 'Mushroom':
			pizza = MushroomTopping(pizza)
		elif topping == 'Pepper':
			pizza = PepperToping(pizza)

	print("Description:", " and ".join(pizza.get_description().rsplit(", ", 1)))
	print("Total Cost:",pizza.get_cost())

if __name__ == "__main__":
	cli()