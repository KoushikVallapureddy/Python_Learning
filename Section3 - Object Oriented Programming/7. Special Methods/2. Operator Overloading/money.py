class Money:
    def __init__(self, amount, currency):
        self.amount = float(amount)
        self.currency = str(currency)
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __mul__(self, scalar):
        return Money(self.amount * scalar, self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    
    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"