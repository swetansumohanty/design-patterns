"""
Decorator Design Pattern
========================
Decorator is a structural pattern that allows to modify the behavior of the objects dynamically 
by placing them inside wrapper object called decorator.
"""

#coffee interface
class Coffee:
    def cost(self):
        pass

    def description(self):
        pass


# concrtete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 10
    
    def description(self):
        return "simple coffee"
    

# coffee decorator
class CoffeeDecorator(Coffee):
    def __init__(self,coffee_decorator):
        self._coffee_decorator = coffee_decorator

    def cost(self):
        return self._coffee_decorator.cost()
    
    def description(self):
        return self._coffee_decorator.description()
    

class MilkCoffee(CoffeeDecorator):
    def __init__(self, coffee_decorator):
        super().__init__(coffee_decorator)

    def cost(self):
        return super().cost() + 5
    
    def description(self):
        return super().description() + " + milk"
    
class ChocolateCoffee(CoffeeDecorator):
    def __init__(self, coffee_decorator):
        super().__init__(coffee_decorator)

    def cost(self):
        return super().cost() + 10
    
    def description(self):
        return super().description() + " + chocolate"
    

simple_coffee :SimpleCoffee = SimpleCoffee()
simple_coffee_cost = simple_coffee.cost()
simple_coffee_desc = simple_coffee.description()

print('simple coffee cost :', simple_coffee_cost)
print('simple coffee desc :', simple_coffee_desc)

milk_coffee = MilkCoffee(simple_coffee)
milk_coffee_cost = milk_coffee.cost()
milk_coffee_desc = milk_coffee.description()

print("milk coffee cost :", milk_coffee_cost)
print("milk coffee description :", milk_coffee_desc)

chocolate_coffee :ChocolateCoffee = ChocolateCoffee(MilkCoffee(SimpleCoffee()))
chocolate_coffee_cost = chocolate_coffee.cost()
chocolate_coffee_desc = chocolate_coffee.description()

print("chocolate coffee cost :", chocolate_coffee_cost)
print("chocolate coffee description :", chocolate_coffee_desc)