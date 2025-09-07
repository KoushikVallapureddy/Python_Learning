from printablemixin import PrintableMixin
from discountmixin import DiscountMixin

class Product(PrintableMixin, DiscountMixin):
    
    def __init__(self, name, price):
        self.name = name
        self.price = price