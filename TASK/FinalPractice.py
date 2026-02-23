# =============================================
# 🧑‍💻 PYTHON OOP PRACTICE — FILL IN THE BLANKS
# =============================================
# Replace every ___ with the correct code!
# Then run this file to check if it works!

# =============================================
# PART 1: Basic Python — Function + List
# =============================================

# Task: Create a function that takes a list of numbers
# and returns ONLY the even numbers in a NEW list


def get_even_numbers(numbers):  # Q1: what parameter name?
    result = []  # Q2: start with empty list
    for num in numbers:  # Q3: loop through what?
        if num % 2 == 0:  # Q4: what operator checks remainder?
            result.append(num)  # Q5: what method adds to list?
    return result  # Q6: return what?


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_numbers(numbers))
# Expected: [2, 4, 6, 8, 10]


# =============================================
# PART 2: Class & Object — Phone class
# =============================================

# Task: Create a Phone class with brand, model, price
# Method: show_info() prints all details


class Phone:  # Q7: class name?
    def __init__(self, brand, model, price):  # Q8: constructor name?
        self.brand = brand  # Q9: store brand
        self.model = model  # Q10: store model
        self.price = price  # Q11: store price

    def show_info(self):  # Q12: what parameter?
        print(f"Phone: {self.brand} {self.model}")  # Q13: brand and model
        print(f"Price: Rs.{self.price}")  # Q14: price


p1 = Phone("Samsung", "Galaxy S24", 79999)  # Q15: create object
p2 = Phone("Apple", "iPhone 15", 129999)  # Q16: create object
p1.show_info()  # Q17: call method
p2.show_info()  # Q18: call method


# =============================================
# PART 3: Encapsulation — Password Manager
# =============================================

# Task: Create a class with a PRIVATE password
# Only allow access through getter/setter methods


class PasswordManager:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Q19: make it private (what prefix?)

    def get_password(self):
        return "Access Denied! Use verify method."

    def verify_password(self, attempt):
        if attempt == self.__password:  # Q20: access private attribute
            print("Password Correct! ✅")
        else:  # Q21: what keyword for fallback?
            print("Wrong Password! ❌")


pm = PasswordManager("suyash", "python123")
print(pm.username)
pm.verify_password("python123")
pm.verify_password("wrong")
# Expected:
# suyash
# Password Correct! ✅
# Wrong Password! ❌


# =============================================
# PART 4: Inheritance — Employee System
# =============================================

# Task: Create Employee (parent) → Manager (child)
# Manager has extra attribute: team_size


class Employee:
    def __init__(self, name, salary):  # Q22: constructor
        self.name = name
        self.salary = salary

    def details(self):
        print(f"Name: {self.name}")
        print(f"Salary: Rs.{self.salary}")


class Manager(Employee):  # Q23: inherits from what?
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Q24: call parent constructor
        self.team_size = team_size

    def details(self):  # overrides parent
        super().details()  # Q25: call parent's details first
        print(f"Team Size: {self.team_size}")


m = Manager("Suyash", 50000, 10)
m.details()
# Expected:
# Name: Suyash
# Salary: Rs.50000
# Team Size: 10


# =============================================
# PART 5: Polymorphism — Payment System
# =============================================

# Task: Different payment methods, same method name


class CreditCard:
    def pay(self, amount):
        print(f"Paid Rs.{amount} via Credit Card 💳")


class UPI:
    def pay(self, amount):  # Q26: same method name as above
        print(f"Paid Rs.{amount} via UPI 📱")


class Cash:
    def pay(self, amount):  # Q27: same method name
        print(f"Paid Rs.{amount} via Cash 💵")


methods = [CreditCard(), UPI(), Cash()]  # Q28: create objects of all 3
for method in methods:
    method.pay(500)  # Q29: call the common method
# Expected:
# Paid Rs.500 via Credit Card 💳
# Paid Rs.500 via UPI 📱
# Paid Rs.500 via Cash 💵


# =============================================
# PART 6: Abstraction — Notification System
# =============================================

from abc import ABC, abstractmethod  # Q30: import module and classes


class Notification(ABC):  # Q31: inherit from what?
    @abstractmethod  # Q32: what decorator?
    def send(self, message):
        pass


class Email(Notification):  # Q33: inherits from?
    def send(self, message):  # Q34: implement the ABSTRACT method!
        print(f"Email sent: {message} 📧")


class SMS(Notification):  # Q35: inherits from?
    def send(self, message):  # Q36: implement the ABSTRACT method!
        print(f"SMS sent: {message} 📲")


e = Email()
e.send("Hello Suyash!")  # Q37: create object, then call method
s = SMS()
s.send("Your OTP is 1234")  # Q38: send is the METHOD name!

# HINT for Q37-Q38:
# First create object: e = Email()
# Then call method: e.send("Hello Suyash!")


# =============================================
# 🏁 IF ALL OUTPUTS ARE CORRECT, YOU PASSED!
# =============================================
