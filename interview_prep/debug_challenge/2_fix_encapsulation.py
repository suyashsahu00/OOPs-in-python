# =============================================
# 🐛 DEBUG CHALLENGE 2: Encapsulation
# =============================================
# This code has 5 BUGS! Find and fix them ALL.
# Expected Output:
# Deposited Rs.500 ✅
# Deposited Rs.300 ✅
# Invalid amount! ❌
# Balance: Rs.800
# =============================================


class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance+=amount
            print(f"Deposited Rs.{amount} ✅")
        else:
            print("Invalid amount! ❌")

    def get_balance(self):
        return self.__balance


acc = BankAccount()
acc.deposit(500)
acc.deposit(300)
acc.deposit(-100)
print(f"Balance: Rs.{acc.get_balance()}")
