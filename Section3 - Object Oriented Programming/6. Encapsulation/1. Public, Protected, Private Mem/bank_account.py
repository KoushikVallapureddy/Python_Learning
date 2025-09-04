class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self._transaction_count = 0
        self.__balance = 0
        self.__account_number = account_number
    
    # Public methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._update_transaction_count()
            return self.__balance
        return None
    
    def get_balance(self):
        return self.__balance
    
    # Protected method
    def _update_transaction_count(self):
        self._transaction_count += 1
