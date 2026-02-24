# ================================================================
# 5️⃣ ABSTRACTION
# ================================================================
# 📢 INTERVIEW ANSWER:
# "Abstraction means hiding complex implementation and showing only
#  the essential features. We use Abstract Base Classes (ABC) to create
#  a template that forces child classes to implement certain methods.
#  You CANNOT create an object of an abstract class."

from abc import ABC, abstractmethod  # 🏷️ abc MODULE: Abstract Base Class module

# 🏷️ ABC: class to inherit from for abstraction
# 🏷️ abstractmethod: decorator that forces implementation


class Shape(ABC):  # 🏷️ ABSTRACT CLASS: inherits from ABC
    @abstractmethod  # 🏷️ DECORATOR: marks method as "must implement in child"
    def area(self):  # 🏷️ ABSTRACT METHOD: no code here, child MUST define it
        pass  # 🏷️ pass: empty placeholder — no logic in parent


class Circle(Shape):  # Child inherits from abstract Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # 🏷️ IMPLEMENTS the abstract method (REQUIRED!)
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  # Must implement or Python throws TypeError!
        return self.side * self.side


# s = Shape()                      # ❌ TypeError! Can NEVER create object of abstract class!
c = Circle(5)
sq = Square(4)
print(f"Circle area: {c.area()}")  # OUTPUT: Circle area: 78.5
print(f"Square area: {sq.area()}")  # OUTPUT: Square area: 16

# ================================================================
# 📌 TERMS USED:
# abc Module         → from abc import ABC, abstractmethod
# ABC                → Abstract Base Class — parent for abstract classes
# @abstractmethod    → Decorator — forces child to implement this method
# Abstract Class     → Template class — can't create its object
# Abstract Method    → Method with no body — child MUST define it
# pass               → Placeholder — means "nothing here"
# Concrete Class     → Normal class that implements all methods (Circle, Square)
# ================================================================
