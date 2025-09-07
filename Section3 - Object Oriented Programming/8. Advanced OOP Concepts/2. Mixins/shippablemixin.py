class ShippableMixin:
    def set_weight(self, weight):
        self.weight = weight
    
    def calculate_shipping(self):
        return self.weight * 0.5