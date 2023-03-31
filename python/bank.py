
class BankAccount:
    
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "completed.")
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "completed.")
        else:
            print("Insufficient balance.")
    
    def print_balance(self):
        print("Current balance:", self.balance)
#Here, we define a class called BankAccount with an __init__ method to initialize the balance to 0. We then define three methods:

#We can create an instance of the BankAccount class and call its methods like this:
# create an instance of BankAccount
account = BankAccount()

# deposit some money
account.deposit(1000)

# withdraw some money
account.withdraw(500)

# try to withdraw more money than the balance
account.withdraw(100)

# print the balance
account.print_balance()

