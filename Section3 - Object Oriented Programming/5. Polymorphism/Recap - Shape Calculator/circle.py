# TODO: Import the Shape class from shape.py
from shape import Shape

# TODO: Import the math module for pi
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius}"