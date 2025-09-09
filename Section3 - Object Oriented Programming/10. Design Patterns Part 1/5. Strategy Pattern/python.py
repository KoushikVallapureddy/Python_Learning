from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        
    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card: {self.card_number}")
        return True

class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal account: {self.email}")
        return True

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
    
    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def checkout(self):
        total = sum(item["price"] for item in self.items)
        if self.payment_strategy:
            return self.payment_strategy.pay(total)
        else:
            raise ValueError("No payment strategy set")

# Create your BitcoinPayment strategy class here
class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
        
    def pay(self, amount):
        print(f"Paying ${amount} using Bitcoin wallet: {self.wallet_address}")
        return True

# Create a main function to demonstrate the strategy pattern
def main():
    # Create a shopping cart
    cart = ShoppingCart()
    
    # Add items to the cart
    cart.add_item("Laptop", 1200)
    cart.add_item("Headphones", 100)
    
    # Create a BitcoinPayment with the specified wallet address
    bitcoin_payment = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    
    # Set the payment strategy
    cart.set_payment_strategy(bitcoin_payment)
    
    # Checkout
    cart.checkout()

if __name__ == "__main__":
    main()