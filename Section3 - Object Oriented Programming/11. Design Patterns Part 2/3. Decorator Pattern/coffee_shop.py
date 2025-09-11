class CoffeeShop:
    """
    A class that manages coffee orders and inventory.
    """
    def __init__(self):
        self.orders = []
    
    def add_order(self, beverage):
        self.orders.append(beverage)
        return len(self.orders)
    
    def get_total_cost(self):
        return sum(beverage.cost() for beverage in self.orders)
    
    def print_orders(self):
        result = []
        for idx, beverage in enumerate(self.orders, start=1):
            result.append(f"Order #{idx}: {beverage.get_description()} - ${beverage.cost():.2f}")
        return "\n".join(result)
    
    def clear_orders(self):
        self.orders = []
    
    def get_order_count(self):
        return len(self.orders)