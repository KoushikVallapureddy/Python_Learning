from product import Product
from shippablemixin import ShippableMixin

class PhysicalProduct(Product, ShippableMixin):
    pass