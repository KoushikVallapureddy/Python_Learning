from bank_account import BankAccount

account1 = BankAccount("Alice Smith", 1000)
account2 = BankAccount("Bob Jones", 2000)

account1.display_info()
account2.display_info()

BankAccount.interest_rate = 0.03

print("After interest rate change:")

account1.display_info()
account2.display_info()