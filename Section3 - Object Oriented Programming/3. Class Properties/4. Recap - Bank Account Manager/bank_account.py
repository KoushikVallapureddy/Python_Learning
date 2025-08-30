class BankAccount:
    # TODO: Define class variable for interest rate (2% = 0.02)
    interest_rate = 0.02
    
    def __init__(self, owner_name, initial_balance):

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__owner_name = owner_name
        self.__balance = initial_balance
    
    @property
    def owner_name(self):
        return self.__owner_name
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative")
            return
        self.__balance = value
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        self.__balance += amount
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if amount > self.__balance:
            print("Insufficient funds")
            return False
        self.__balance -= amount
        return True
    
    def apply_interest(self):
        interest = self.__balance * BankAccount.interest_rate
        self.__balance += interest
        return interest
    
    def display_info(self):
        print(f"Account Owner: {self.owner_name}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {BankAccount.interest_rate * 100}%")