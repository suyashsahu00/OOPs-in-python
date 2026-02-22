class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi I am {self.name} and I am {self.age} years old.")
    def birthday(self):
        self.age = self.age +1
        print(f"Happy Birthday {self.name}! You are now {self.age} year old")



p1 = Person("Suyash", 21)
p2 = Person("Rahul", 22)
p1.introduce()  # prints automatically!
p2.introduce()  # prints automatically!
print(p1.age) # before
p1.birthday() # Call birthday
print(p1.age) # after - should be +1