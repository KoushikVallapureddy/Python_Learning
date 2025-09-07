from deco import add_counter

@add_counter
class Calculator:
    def __init__(self):
        ...
        
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b
