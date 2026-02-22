class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi I am {self.name} and I am {self.age} years old.")


p1 = Person("Suyash", 21)
p2 = Person("Rahul", 22)
p1.introduce()  # prints automatically!
p2.introduce()  # prints automatically!
