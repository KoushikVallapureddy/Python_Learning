from paymentmethod import PaymentMethod

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
        super().__init__()
    
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"
    
    def payment_details(self):
        masked_number = "*" * (len(self.card_number) - 4) + self.card_number[-4:]
        return f"Credit Card: {masked_number}"