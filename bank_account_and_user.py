class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0, balance=0):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: charging a $5 fee.")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}'s balance is {self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self


# account1 = BankAccount(0.04, 50)
# account2 = BankAccount(0.03, 150)
user_peyton = User("Peyton", "peyton@codingdojo.com",)
user_chris = User("Chris", "chris@halfcabstudios.com")
user_monty = User("Monty", "montypython@python.com")


user_peyton.make_deposit(300)
user_chris.make_deposit(500).transfer_money(
    user_peyton, 250).display_user_balance()
user_peyton.display_user_balance()

# account1.deposit(25).deposit(42).deposit(35).withdraw(
#     75).yield_interest().display_account_info()

# account2.deposit(150).deposit(50).withdraw(150).withdraw(70).withdraw(
#     25).withdraw(100).yield_interest().display_account_info()
