class UnknownShape:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def area(self):
        return self.size ** 2
    
    def perimeter(self):
        return 4 * self.size
    
    def describe(self):
        return f"This is a {self.name} shape with area {self.area()} and perimeter {self.perimeter()}"
    
    def __str__(self):
        return f"{self.name} with size {self.size}"