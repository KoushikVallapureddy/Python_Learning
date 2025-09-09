from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

class ShapeFactory:
    
    def create_shape(self, shape_type, *args):
        shape_type = shape_type.lower()
        if shape_type == "circle":
            return Circle(args[0])
        elif shape_type == "rectangle":
            return Rectangle(args[0], args[1])
        elif shape_type == "triangle":
            return Triangle(args[0], args[1], args[2])
        else:
            raise ValueError(f"Invalid shape type: {shape_type}")