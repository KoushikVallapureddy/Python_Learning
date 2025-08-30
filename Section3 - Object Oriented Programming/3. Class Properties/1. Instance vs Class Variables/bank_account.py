#Challenge:
'''
Complete a banking system.. You'll define a BankAccount class in one file and use it in another.
You'll work with:
    bank_account.py: Define the BankAccount class with attributes and methods
    driver.py: Import the class, create accounts, and demonstrate class variables
    
Follow the TODO comments in both files for step-by-step instructions. The comments will guide you through creating the class with proper variables, methods, and showing how class variables affect all instances.
'''

class BankAccount:
    interest_rate = 0.02
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def display_info(self):
        print(f"Account: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {BankAccount.interest_rate * 100}%")
        print()