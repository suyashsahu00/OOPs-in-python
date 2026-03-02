# =============================================
# 🐛 DEBUG CHALLENGE 5: Abstraction
# =============================================
# This code has 5 BUGS! Find and fix them ALL.
# Expected Output:
# Circle area: 78.5
# Square area: 16
# =============================================

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # SAME name as parent!
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


c = Circle(5)
s = Square(4)
print(f"Circle area: {c.area()}")  # SAME method name!
print(f"Square area: {s.area()}")
