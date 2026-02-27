# =============================================
# INTERVIEW TASK 6: Banking System (COMBO!)
# =============================================
# This combines: Class + Encapsulation + Inheritance
#
# Instructions:
# 1. Create class Account with PRIVATE __balance (starts at 0)
# 2. deposit(amount) → adds money, prints "Deposited Rs.X ✅"
# 3. withdraw(amount) → removes money if enough balance,
#    else prints "Insufficient balance! ❌"
# 4. get_balance() → returns private balance
# 5. Create SavingsAccount(Account) with extra attribute interest_rate
# 6. add_interest() → calculates interest and adds to balance
#    (interest = balance * interest_rate / 100)
#
# Expected Output:
# Deposited Rs.1000 ✅
# Deposited Rs.500 ✅
# Withdrawn Rs.300 ✅
# Insufficient balance! ❌
# Balance: Rs.1200
# Interest added at 10% ✅
# Balance after interest: Rs.1320.0
# =============================================

# Write your code below 👇


class Account:
    def __init__(self):  # no parameter, balance starts at 0
        self.__balance = 0

    def deposit(self, amount):  # not "deposite"!
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount} ✅")  # amount = parameter

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            print(f"Withdrawn Rs.{amount} ✅")  # amount, not self.amount!
        else:
            print("Insufficient balance! ❌")

    def get_balance(self):
        return self.__balance  # return the value, not a formatted string


class SavingsAccount(Account):  # CHILD inherits from Account!
    def __init__(self, interest_rate):
        super().__init__()  # call parent constructor
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100  # use getter!
        self.deposit(interest)  # reuse parent's deposit method!
        print(f"Interest added at {self.interest_rate}% ✅")


sa = SavingsAccount(10)  # 10% interest rate
sa.deposit(1000)
sa.deposit(500)
sa.withdraw(300)
sa.withdraw(5000)  # should fail!
print(f"Balance: Rs.{sa.get_balance()}")
sa.add_interest()
print(f"Balance after interest: Rs.{sa.get_balance()}")
