class Bank:
    def __init__(self, initial_amount=0.0):
        self.balance = initial_amount
    def transaction_log(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string}\tRemaining amount: {self.balance}\n")
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount;
            self.transaction_log(f"Withdrew {amount}")
        else:
            print('not enough money in your account')
    def deposit(self, amount):
        self.balance = self.balance + amount;
        self.transaction_log(f"Deposited {amount}")

account = Bank(100)
while True:
    action = input("What action would you like to take")
    if action in ["withdraw", "deposit"]:
        if action == "withdraw":
            account.withdraw(input("how much do you want to withdraw?"))
        if action == "deposit":
            account.deposit(input("how much do you want to withdraw?"))
        print(f"Your balance is now {account.balance}")
        