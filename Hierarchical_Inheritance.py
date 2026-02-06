#Hierarchical inheritance is a type of inheritance where one parent class is inherited by multiple child classes.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest Added:", interest)

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Amount Withdrawn using Overdraft:", amount)
        else:
            print("Overdraft Limit Exceeded")

s1 = SavingsAccount("Ramya", 5000, 5)
s1.deposit(1000)
s1.add_interest()
s1.withdraw(2000)
s1.display_balance()

print("---------------------")

c1 = CurrentAccount("Anu", 3000, 2000)
c1.deposit(500)
c1.withdraw_with_overdraft(4500)
c1.display_balance()
