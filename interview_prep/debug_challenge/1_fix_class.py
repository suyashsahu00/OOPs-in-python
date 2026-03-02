# =============================================
# 🐛 DEBUG CHALLENGE 1: Class & Object
# =============================================
# This code has 5 BUGS! Find and fix them ALL.
# Expected Output:
# Toyota Camry - Rs.1500000
# Honda City - Rs.1200000
# Total cars created: 2
# =============================================


class car:
    total_cars = 0

    def _init_(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        car.total_cars += 1

    def show():
        print(f"{self.brand} {self.model} - Rs.{self.price}")


c1 = car("Toyota", "Camry", 1500000)
c2 = car("Honda", "City", 1200000)
c1.show()
c2.show()
print(f"Total cars created: {total_cars}")
