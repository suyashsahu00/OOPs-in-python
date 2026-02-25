# =============================================
# INTERVIEW TASK 2: Encapsulation
# =============================================
# Instructions:
# 1. Create a class called Wallet
# 2. Make balance PRIVATE (double underscore), starting at 0
# 3. Add method add_money(amount) — adds money if amount > 0, else print error
# 4. Add method check_balance() — returns the private balance
# 5. Test it!
#
# Expected Output:
# Added Rs.500 ✅
# Added Rs.300 ✅
# Invalid amount! ❌
# Balance: Rs.800
# =============================================

# Write your code below 👇
class Wallet:
    def __init__(self, balance):
        self.__balance = balance
        self.__balance = 0
    def add_money(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added Rs.{self.__balance}")
        else:
            print("Invalid amount!")
    def check_balance(self):
        return self.__balance

acc = Wallet(1000)
acc.add_money(500)
acc.add_money(300)
acc.add_money(-1)
print(f"Balance: Rs.{acc.check_balance()}")
# acc.check_balance()

