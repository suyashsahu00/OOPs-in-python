# =============================================
# 🐛 DEBUG CHALLENGE 5: Abstraction
# =============================================
# This code has 5 BUGS! Find and fix them ALL.
# Expected Output:
# Circle area: 78.5
# Square area: 16
# =============================================

from abc import ABC


class Shape(ABC):
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return 3.14 * radius * radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


c = Circle(5)
s = Square(4)
print(f"Circle area: {c.circle_area()}")
print(f"Square area: {s.area()}")
