from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side  # fixed: sef → self

    def area(self):
        print(
            f"Square area: {self.side * self.side}"
        )  # fixed: use self.side not self.area


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(
            f"Triangle area: {0.5 * self.base * self.height}"
        )  # fixed: use self.base & self.height


sq = Square(5)
tr = Triangle(4, 5)
sq.area()
tr.area()  # fixed: added ()
