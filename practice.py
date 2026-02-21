# class =  Blueprint (define structure & behavior)
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def describe(self):
        print(f"{self.brand} goest at {self.speed} km/hr")

# Object = instance (actual thing created from the blueprint)

car1 = Car("Toyota", 120)
car2 = Car("Audio",140)

car1.describe()
car2.describe()