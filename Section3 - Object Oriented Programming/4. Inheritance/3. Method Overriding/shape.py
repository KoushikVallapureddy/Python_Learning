'''
In this challenge, you'll implement a shape hierarchy.
    shape.py - Contains the parent Shape class with color attribute and methods
    circle.py - Contains the Circle class that inherits from Shape
    square.py - Contains the Square class that inherits from Shape
Each file contains detailed TODO comments that will guide you step-by-step through the implementation.
'''

import math

class Shape:
    def __init__(self, color):
        # TODO: Initialize the Shape class with color parameter
        # TODO: Store color as instance attribute (self.color)
        self.color = color
    
    def area(self):
        # TODO: Return 0 as a placeholder for child classes to override
        return 0
    
    def describe(self):
        # TODO: Print a description of the shape
        # TODO: Format should be exactly: "This is a {self.color} shape."
        print(f"This is a {self.color} shape.")