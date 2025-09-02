class ShapeCalculator:
    def process_shape(self, shape):
        print(f"Processing: {shape}")
        print(shape.describe())
        return {
            "area": shape.area(),
            "perimeter": shape.perimeter()
        }