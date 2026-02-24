# =============================================
# Q10: isinstance() — Type Checking
# =============================================
# Task: Create Animal → Dog, Cat classes
# Use isinstance() to check what type each object is
# isinstance(object, ClassName) → returns True or False

class Animal:
    def __init__(self, name):                # Q1
        self.name = name                     # Q2

class Dog(Animal):                          # Q3: inherits from?
    def __init__(self, name, breed):          # Q4
        super().__init__(name)                    # Q5: call parent constructor
        self.breed = breed                     # Q6: store breed

    def bark(self):
        print(f"{self.name} says Woof! 🐕")

class Cat(Animal):                          # Q7: inherits from?
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print(f"{self.name} says Meow! 🐱")

# Create objects
d = Dog("Buddy", "Labrador")
c = Cat("Whiskers")

# Type checking with isinstance()
print(isinstance(d, Dog))       # Q8: is d a Dog? → True
print(isinstance(c, Cat))       # Q9: is c a Cat? → True
print(isinstance(d, Animal))       # Q10: is d an Animal? → True (because Dog inherits from Animal!)
print(isinstance(c, Dog))       # Q11: is c a Dog? → False (Cat is NOT a Dog!)

d.bark()
c.meow()
