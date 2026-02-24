# ================================================================
# 2️⃣ ENCAPSULATION
# ================================================================
# 📢 INTERVIEW ANSWER:
# "Encapsulation means hiding internal data and only allowing access
#  through methods. We use private attributes (double underscore __)
#  to restrict direct access. This protects data from accidental changes."


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 🏷️ PRIVATE ATTRIBUTE: __ prefix hides it from outside

    def deposit(
        self, amount
    ):  # 🏷️ SETTER/MODIFIER: controlled way to change private data
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount} ✅")

    def get_balance(self):  # 🏷️ GETTER: controlled way to READ private data
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)  # OUTPUT: Deposited Rs.500 ✅
print(f"Balance: Rs.{acc.get_balance()}")  # OUTPUT: Balance: Rs.1500
# print(acc.__balance)             # ❌ ERROR! Can't access private directly

# ================================================================
# 📌 TERMS USED:
# Private Attribute → self.__balance (__ makes it private/hidden)
# Getter Method     → get_balance() — reads private data safely
# Setter Method     → deposit() — modifies private data with validation
# Data Hiding       → Outside code can't directly touch __balance
# ================================================================
