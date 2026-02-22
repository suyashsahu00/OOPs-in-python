class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")
d = Dog("Tommy")
d.eat() # inherited from Animal
d.bark() # Dog's own method!