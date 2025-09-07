from product import Product

class DigitalProduct(Product):
    
    def apply_discount(self, percent):
        return self.price * 0.9