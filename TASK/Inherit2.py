class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def info(self):
        print(f"Brnad: {self.brand} | Speed: {self.speed} Km/h")


class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery):  # __ on BOTH sides!
        super().__init__(brand, speed)
        self.battery = battery  # fixed typo: battry → battery

    def info(self):  # overides parent's info()
        super().info()
        print(f"Battery: {self.battery} KWh")


car = ElectricCar("Tesla", 200, 100)
car.info()
