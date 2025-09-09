from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        raise NotImplementedError("Subclasses must implement area()")
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        raise NotImplementedError("Subclasses must implement perimeter()")