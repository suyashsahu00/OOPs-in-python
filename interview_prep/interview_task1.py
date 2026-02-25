# =============================================
# INTERVIEW TASK 1: Class & Object
# =============================================
# Instructions:
# 1. Create a class called Phone
# 2. Add a constructor (__init__) that takes brand, model, price
# 3. Store all 3 as attributes
# 4. Create a method info() that prints: "Samsung Galaxy S24 - Rs.79999"
# 5. Create 2 objects with different phone data
# 6. Call info() on both objects
#
# Expected Output:
# Samsung Galaxy S24 - Rs.79999
# Apple iPhone 15 - Rs.129999
# =============================================

# Write your code below 👇
class Phone: 
    def __init__(self, brand, model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def info(self):
        print(f"{self.brand} {self.model} - Rs.{self.price}")
s1 = Phone("Samsung Galaxy","S24","79999")
s2 = Phone("Apple iPhone", "15" ,"129999")
s1.info()
s2.info()