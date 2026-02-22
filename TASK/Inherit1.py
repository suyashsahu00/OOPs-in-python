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

class GuideDog(Dog):
    def __init__(self,name,owner):
        super().__init__(name) # pass name up to Animal
        self.owner = owner # extra attribute
    def guide(self):
        print(f"{self.name} is guiding {self.owner}")
g = GuideDog("Tommy", "Suyash")
g.eat() # from Animal ^^
g.bark() # from Dog ^
g.guide() # own method 