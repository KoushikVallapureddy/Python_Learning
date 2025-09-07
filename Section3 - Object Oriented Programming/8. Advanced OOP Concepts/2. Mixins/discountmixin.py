class DiscountMixin:
    def apply_discount(self, percent):
        discounted_price = self.price - (self.price * percent / 100)
        return discounted_price