from abc import ABC, abstractmethod


# ABSTRACT class — acts as template
class Vehicle(ABC):
    @abstractmethod  # forces ALL child classes to implement start()
    def start(self):
        pass  # no code here — child must define it!


# Child class — IMPLEMENTS the abstract method
class Car(Vehicle):
    def start(self):  # no @abstractmethod here! just implement it!
        print("Car engine starts: Vroom! 🚗")


class Bike(Vehicle):
    def start(self):  # must implement or Python will give error!
        print("Bike engine starts: Vroom Vroom! 🏍️")


# v = Vehicle()  ← ❌ Can't create object of abstract class!
car = Car()  # ✅
bike = Bike()  # ✅

car.start()
bike.start()
