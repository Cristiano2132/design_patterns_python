from abc import ABC, abstractmethod

class ICoffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    def get_tax(self):
        return 0.1 * self.get_cost()

class Coffee(ICoffee):
    def get_cost(self):
        return 1.00

    def get_ingredients(self):
        return 'coffee'

class CoffeeDecorator(ICoffee):
    def __init__(self, decorated_coffee: ICoffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()

class Sugar(CoffeeDecorator):
    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', sugar'

class Milk(CoffeeDecorator):
    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', milk'

class Vanilla(CoffeeDecorator):
    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', vanilla'

if __name__ == "__main__":
    my_coffee = Coffee()
    print(f'Ingredients: {my_coffee.get_ingredients()}; Cost: {my_coffee.get_cost()}; Sales tax = {my_coffee.get_tax()}')

    my_coffee = Milk(my_coffee)
    print(f'Ingredients: {my_coffee.get_ingredients()}; Cost: {my_coffee.get_cost()}; Sales tax = {my_coffee.get_tax()}')

    my_coffee = Vanilla(my_coffee)
    print(f'Ingredients: {my_coffee.get_ingredients()}; Cost: {my_coffee.get_cost()}; Sales tax = {my_coffee.get_tax()}')

    my_coffee = Sugar(my_coffee)
    print(f'Ingredients: {my_coffee.get_ingredients()}; Cost: {my_coffee.get_cost()}; Sales tax = {my_coffee.get_tax()}')
