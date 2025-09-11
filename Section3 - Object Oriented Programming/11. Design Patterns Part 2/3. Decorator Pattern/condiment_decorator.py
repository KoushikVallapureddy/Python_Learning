from beverage import Beverage
from abc import abstractmethod

class CondimentDecorator(Beverage):
    """
    Abstract decorator class for all condiments.
    """
    @abstractmethod
    def get_description(self):
        pass  # Abstract, subclasses will implement


class Milk(CondimentDecorator):
    """
    Concrete decorator for adding milk to a beverage.
    """
    def __init__(self, beverage):
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + " + Milk"
    
    def cost(self):
        return self.beverage.cost() + 0.10


class Mocha(CondimentDecorator):
    """
    Concrete decorator for adding mocha to a beverage.
    """
    def __init__(self, beverage):
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + " + Mocha"
    
    def cost(self):
        return self.beverage.cost() + 0.20


class Soy(CondimentDecorator):
    """
    Concrete decorator for adding soy to a beverage.
    """
    def __init__(self, beverage):
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + " + Soy"
    
    def cost(self):
        return self.beverage.cost() + 0.15


class Whip(CondimentDecorator):
    """
    Concrete decorator for adding whipped cream to a beverage.
    """
    def __init__(self, beverage):
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + " + Whip"
    
    def cost(self):
        return self.beverage.cost() + 0.10