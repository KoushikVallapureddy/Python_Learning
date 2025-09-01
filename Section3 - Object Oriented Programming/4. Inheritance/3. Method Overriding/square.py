from shape import Shape

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def describe(self):
        print(f"This is a {self.color} square with side length {self.side_length}.")