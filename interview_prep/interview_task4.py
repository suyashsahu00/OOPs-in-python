# =============================================
# INTERVIEW TASK 4: Polymorphism
# =============================================
# Instructions:
# 1. Create 3 classes: Car, Bike, Truck
# 2. Each class has a fuel_type() method that prints different fuel info
# 3. Create a list with one object of each class
# 4. Loop through the list and call fuel_type() on each
#
# Expected Output:
# Car runs on Petrol ⛽
# Bike runs on Petrol ⛽
# Truck runs on Diesel ⛽
# =============================================

# Write your code below 👇
class Car:
    def fuel_type(self):
        print("Car runs on Petrol ⛽")

class Bike:
    def fuel_type(self):
        print("Bike runs on Petrol ⛽")

class Truck:
    def fuel_type(self):
        print("Truck runs on Diesel ⛽")

vehicals = [Car(), Bike(), Truck()]
for vehical in vehicals:
    vehical.fuel_type()

