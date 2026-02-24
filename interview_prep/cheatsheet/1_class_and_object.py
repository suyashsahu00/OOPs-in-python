# ================================================================
# 1️⃣ CLASS & OBJECT
# ================================================================
# 📢 INTERVIEW ANSWER:
# "A Class is a blueprint/template for creating objects.
#  An Object is an instance of a class — a real thing created from the blueprint.
#  Think of Class as a form template, and Object as a filled form."


class Car:  # 🏷️ CLASS: blueprint/template
    def __init__(self, brand):  # 🏷️ __init__: constructor — runs when object is created
        self.brand = (
            brand  # 🏷️ self.brand: instance attribute — data stored in the object
        )
        # 🏷️ self: refers to the CURRENT object being created

    def drive(self):  # 🏷️ METHOD: a function inside a class
        print(f"{self.brand} is driving 🚗")


# Creating objects (instances)
car1 = Car("Toyota")  # 🏷️ OBJECT: real instance created from the class
car2 = Car("BMW")  # Each object has its OWN brand value
car1.drive()  # OUTPUT: Toyota is driving 🚗
car2.drive()  # OUTPUT: BMW is driving 🚗

# ================================================================
# 📌 TERMS USED:
# Class     → Blueprint/template for creating objects
# Object    → Real instance created from a class (car1, car2)
# __init__  → Constructor — runs automatically when object is created
# self      → Refers to the CURRENT object
# Attribute → Data stored in object (self.brand)
# Method    → Function inside a class (drive)
# ================================================================
