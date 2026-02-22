class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self,amount):
        self.__balance = self.__balance + amount
        print(f"New balance: {self.__balance}")

    def get_balance(self):
        print(f"Balance: {self.__balance}")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance = self.__balance - amount
            print(f"Withdrawn! New balance: {self.__balance}")


acc = BankAccount()
acc.get_balance()  # 1000
acc.deposit(500)
acc.get_balance()
acc.withdraw(200)
acc.withdraw(2000)