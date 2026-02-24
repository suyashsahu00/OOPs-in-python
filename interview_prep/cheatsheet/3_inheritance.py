# ================================================================
# 3️⃣ INHERITANCE
# ================================================================
# 📢 INTERVIEW ANSWER:
# "Inheritance allows a child class to inherit attributes and methods
#  from a parent class. This promotes code reuse — we don't rewrite
#  common code. The child can also add its own features or override
#  parent methods."


class Animal:  # 🏷️ PARENT CLASS (also called Base/Super class)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):  # 🏷️ CHILD CLASS: inherits from Animal using (Animal)
    def __init__(self, name, breed):
        super().__init__(name)  # 🏷️ super(): calls PARENT's constructor
        # 🏷️ __init__(name): passes name to parent to store
        self.breed = breed  # Child's OWN extra attribute

    def speak(self):  # 🏷️ METHOD OVERRIDE: redefines parent's method
        print(f"{self.name} says Woof! 🐕")


dog = Dog("Buddy", "Labrador")
dog.speak()  # OUTPUT: Buddy says Woof! 🐕 (uses CHILD's version)
print(f"Breed: {dog.breed}")  # OUTPUT: Breed: Labrador

# ================================================================
# 📌 TERMS USED:
# Parent Class     → Base class that others inherit from (Animal)
# Child Class      → Class that inherits — class Dog(Animal)
# super()          → Gives access to parent class
# super().__init__()→ Calls parent's constructor (with () after super!)
# Method Override  → Child redefines parent's method with same name
# Code Reuse       → Child gets parent's code without rewriting
# ================================================================
