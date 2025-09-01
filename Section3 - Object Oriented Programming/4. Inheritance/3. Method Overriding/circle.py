import math
from shape import Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def describe(self):
        print(f"This is a {self.color} circle with radius {self.radius}.")