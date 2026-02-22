# Abstraction = Hiding the implementation details and showing only thee essential featueres to the user. 
from abc import ABC, abstractmethod # ABC = Abstract Base class

# Abstract Class - acts as a TEMPLATE
class Animal(ABC):#inherit from ABC
    @abstractmethod #forrces child classs to implement this 
    def sound(self):
        pass #no implementation here!
    @abstractmethod
    def move(self):
        pass
# child class MUST implement all abstract methods
class Dog(Animal):
    def sound(self):
        print("Woof!")
    def move(self):
        print("Dog runs on 4 legs")
class Bird(Animal):
    def sound(self):
        print("Tweet!")

    def move(self):
        print("Bird flies with wings")
#aniimal = Animal( ) Error ! canot instantiate abstract class 
dog = Dog()
dog.sound() # woof
dog.move() #dog runs on 4 legs
