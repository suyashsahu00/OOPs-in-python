# =============================================
# Q05: Polymorphism — Area Calculator
# =============================================
# Task: 3 shape classes, each with area() method
# Loop through all and print areas


class Circle:
    def __init__(self, radius):  # Q1,Q2: parameter is "radius" not "area"!
        self.radius = radius  # Q3: store as self.radius

    def area(self):  # Q4 ✅
        return 3.14 * self.radius * self.radius  # Q5: always self.radius!


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):  # Q6 ✅
        return self.side * self.side  # Q7: self.side not just side!


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Q8 ✅
        return self.length * self.width  # Q9: length × width, not side × side!


# Polymorphism in action!
shapes = [Circle(5), Square(4), Rectangle(6, 3)]  # Q10: no "Rectangle" string!

for i in shapes:  # Q11 ✅
    print(f"Area: {i.area()}")  # Q12: i.area() not self.area()!
