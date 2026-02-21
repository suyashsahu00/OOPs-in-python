# Same method name, different behaviour in each class
class Dog:
    def sound(self):
        print("Woof!")
class Cat:
    def sound(self):
        print("Meow")
class Duck:
    def sound(self):
        print("Quack")

#Polymorphism in action
animals = [Dog(),Cat(),Duck()]
for animal in animals:
    animal.sound() #same method, different output
